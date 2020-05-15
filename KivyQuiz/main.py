##Author: Kieran Thompson
##Date: 17/11/19
##Title: Quiz

import html
import random
import datetime
import json

import kivy
from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

import textfiles

class QuestionOject():

    def __init__(self, requestedObject):
        self._question = html.unescape(requestedObject["results"][0]["question"])
        self._incorrectAnswers = requestedObject["results"][0]["incorrect_answers"]
        self._correct = html.unescape(requestedObject["results"][0]["correct_answer"])
    def getQuestion(self):
        return self._question
    def getCorrectAns(self):
        return self._correct
    def getAllAnswers(self):
        allAns = self._incorrectAnswers 
        allAns.append(self._correct)
        print(allAns)
        random.shuffle(allAns)
        return allAns



def wrap_by_word(s, n):
    '''returns a string where \\n is inserted between every n words'''
    a = s.split()
    ret = ''
    for i in range(0, len(a), n):
        ret += ' '.join(a[i:i+n]) + '\n'

    return ret


class MyGrid(GridLayout):

    def __init__(self, **kwargs):

        #Class values
        self._question = ""
        self._options = []



        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        #Background colour
        with self.canvas.before:
            Color(0.3, 0.3, 0.24, 1)
            self.rect = Rectangle(size=(800,800), pos=(0,0))

        self.inside = GridLayout()
        self.inside.cols = 2


        #Title
        self.add_widget(Label(text="Quiz question", font_size='20sp',  size_hint_y=None, color=[0,123,1,1]))


        #Question label
        self.question = Label(size_hint_y=None, padding_y=1)
        self.add_widget(self.question)


        self.multipleChoiceQ = Button(text="Get question type Multiple", size_hint_y=None, background_color=(0, 0.3, 0.65, 1))
        self.multipleChoiceQ.bind(on_press=self.questionDisplay)
        self.TrueFalseQ = Button(text="Get question type T/F", size_hint_y=None, background_color=(0.65, 0.3, 0.2, 1))
        self.TrueFalseQ.bind(on_press=self.questionDisplay)
        self.downloadQ = Button(text="Download a question set", size_hint_y=None, background_color=(0, 0, 0.2, 1))
        self.downloadQ.bind(on_press=self.downloadQuestions)
        self.playDownloadedQ = Button(text="Play a downloaded Question", size_hint_y=None, background_color=(0, 0, 0.2, 1))
        self.playDownloadedQ.bind(on_press=self.getDownloadQ)


        #Answers buttons section
        self.add_widget(self.inside)
       # self.add_widget(Label(text="", font_size='1sp'))


        #Get question area
        self.getQuestionContainer = GridLayout()
        self.getQuestionContainer.cols = 2
        self.getQuestionContainer.add_widget(self.multipleChoiceQ)
        self.getQuestionContainer.add_widget(self.TrueFalseQ)
        self.getQuestionContainer.add_widget(self.downloadQ)
        self.getQuestionContainer.add_widget(self.playDownloadedQ)
        self.add_widget(self.getQuestionContainer)

    def questionDisplay(self, i):
        self.inside.clear_widgets()
        self.question.text = ""

        if("Get question type T/F" == i.text):
            self.getQuestionBool()

        else:
            self.getQuestionMultiple()
        # strat1 = Save()
        # strat1.execute("y")
        # strat1 = Save(textfileSave)
        # strat1.execute()
        #strat1 = Save(csvSave)
        #strat1.execute("q")



    def answerQuestion(self, button):


        print(button.text)
        if(button.text == self.q.getCorrectAns()):
            self.question.text = "Correct"
        else:
            self.question.text = "Incorrect"

        #clear button options
        self.inside.clear_widgets()



        #t = Save()
        #t.execute(self.q.getCorrectAns)

    def getQuestionBool(self):
        url = "https://opentdb.com/api.php?amount=1&type=boolean"
        a = self.make_request(url, self.on_request_success)

    def getQuestionMultiple(self):
        url = "https://opentdb.com/api.php?amount=1&type=multiple"
        a = self.make_request(url, self.on_request_success)

    def downloadQuestions(self, i):
        url = "https://opentdb.com/api.php?amount=1&type=multiple"
        a = self.make_request(url, self.download)



    def on_request_success(self, request, result):
        print(type(result))
        print(result)
        self.q = QuestionOject(result)
        self.question.text = wrap_by_word(self.q.getQuestion(), 6)
        options = self.q.getAllAnswers()
        print(len(options))

        if (2 == len(options)):
            self.inside.add_widget(Button(
                text=html.unescape(options[0]), font_size='15sp', size_hint_y=None, on_press=self.answerQuestion))
            self.inside.add_widget(Button(
                text=html.unescape(options[1]), font_size='15sp', size_hint_y=None, on_press=self.answerQuestion))
        else:
            self.inside.add_widget(Button(
                text=html.unescape(options[0]), font_size='15sp', size_hint_y=None, on_press=self.answerQuestion))
            self.inside.add_widget(Button(
                text=html.unescape(options[1]), font_size='15sp', size_hint_y=None, on_press=self.answerQuestion))
            self.inside.add_widget(Button(
                text=html.unescape(options[2]), font_size='15sp', size_hint_y=None, on_press=self.answerQuestion))
            self.inside.add_widget(Button(
                text=html.unescape(options[3]), font_size='15sp', size_hint_y=None, on_press=self.answerQuestion))


    def download(self, request, result):
        stack = textfiles.downloadStack("f")
        stack.saveItem(result)

    def getDownloadQ(self, i):
        stack = textfiles.downloadStack("f")

        if (0 == stack.getFileSize()):
            self.question.text = "No questions are currently downloaded"

            #clear button options
            self.inside.clear_widgets()
        else:

            ##more here
            downloadQuestion = stack.getItem()

            #clear button options
            self.inside.clear_widgets()

            print(downloadQuestion)
            print(type(downloadQuestion))
            a =  downloadQuestion.replace("\'", "\"")
            print(a)
            self.q = QuestionOject(json.loads(a))
            self.question.text = wrap_by_word(self.q.getQuestion(), 6)

            options = self.q.getAllAnswers()
            print(len(options))

            if (2 == len(options)):
                self.inside.add_widget(Button(
                    text=html.unescape(options[0]), font_size='15sp', size_hint_y=None, on_press=self.answerQuestion))
                self.inside.add_widget(Button(
                    text=html.unescape(options[1]), font_size='15sp', size_hint_y=None, on_press=self.answerQuestion))
            else:
                self.inside.add_widget(Button(
                    text=html.unescape(options[0]), font_size='15sp', size_hint_y=None, on_press=self.answerQuestion))
                self.inside.add_widget(Button(
                    text=html.unescape(options[1]), font_size='15sp', size_hint_y=None, on_press=self.answerQuestion))
                self.inside.add_widget(Button(
                    text=html.unescape(options[2]), font_size='15sp', size_hint_y=None, on_press=self.answerQuestion))
                self.inside.add_widget(Button(
                    text=html.unescape(options[3]), font_size='15sp', size_hint_y=None, on_press=self.answerQuestion))



    def make_request(self, urlString, function):
        req = UrlRequest(
         url         = urlString,
         on_error    = None,
         on_failure  = None,
         on_progress = None,
         on_redirect = None,
         on_success  = function,
         timeout     = 5,
        )



class MyApp(App):
    def build(self):
        return MyGrid()

MyApp().run()

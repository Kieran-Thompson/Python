##Kieran Thompson
##Timer 
from selenium import webdriver
from time import sleep

class WebDriver:

    def __init__(self):
        self._driver = webdriver.Chrome(executable_path='C:\PYTHON\chromedriver.exe')

    def CloseDriver(self):
        self._driver.quit() ##clears the other console also
        return True

    def GoToURL(self, url):
        self._driver.get(url)

    def PressButton(self, XPath):
        self._driver.find_element_by_xpath(XPath).click() 
        return True

   
def GetTimer(mins, secs):
    TotalTimeWaiting = 0
    TotalTimeWaiting = int(mins)
    TotalTimeWaiting = TotalTimeWaiting * 60
    TotalTimeWaiting = TotalTimeWaiting + int(secs)
    sleep(TotalTimeWaiting)
    return True

def Pomodoro():
    GetTimer(25, 0)
    return True

def PlaySongSteps():
    URLSoundBoardHome = "https://www.myinstants.com/instant/dramatic-chipmunk/"
    SoundButton = "/html/body/div[4]/div[3]/div[3]/div[2]"
    
    WebAgent = WebDriver()
    WebAgent.GoToURL(URLSoundBoardHome)
    sleep(10) 
    test = WebAgent.PressButton(SoundButton)
    sleep(5)
    WebAgent.CloseDriver()

def GetTimerValues():
    minutes = ""
    seconds = ""
    while (((not minutes.isdigit()) or (not seconds.isdigit())) and (not "P" == minutes == seconds)):
        print("please enter a time")
        print("Enter \"P\" in both MM and SS to get a Pomodoro Time ")
        minutes = input("MM:")
        seconds = input("SS:")
    print(minutes + " " + seconds)
    Time = (minutes, seconds)
    return Time

def DisplayMessages():
    print("Timer Finshed")

def main():
    Time = GetTimerValues()
    if ("P" == Time[0] == Time[1]):
        Pomodoro()
    else:
        GetTimer(Time[0],Time[1])
    PlaySongSteps()
    DisplayMessages()
    

main()

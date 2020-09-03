##15/08/18

##Kieran Thompson

import requests
from bs4 import BeautifulSoup


#given the url, return the html page parsed as a BSoup object 
def scrapePage(url):
    
    ### get the html data from the webpage page
    webpage = requests.get(url)
    page = BeautifulSoup(webpage.text, 'html.parser')

    return page


##given the html pag and class tag, get the test from the page and return it
def findFromPage(page, tag, class_):

    ##get the word with the tag, from the html doc
    word_tag = page.find(tag, class_)

   
    return word_tag

##given url tag and class
##return text from page
def getDataFromWeb(url, tag, class_):

    page = scrapePage(url)
    data = findFromPage(page, tag, class_)

    ##clean html off data
    data = data.text
    
    return data


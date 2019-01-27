##23/08/18


##Kieran Thompson


import requests
from bs4 import BeautifulSoup


##given the url, return the html page parsed as a BSoup object 
def scrapePage(url):
    
    ### get the html data from the webpage page
    webpage = requests.get(url)
    page = BeautifulSoup(webpage.text, 'html.parser')

    return page


##given the html page, get the text from the page and return it
def findFromPage(page):

    castList = page.find("table", { "class" : "cast_list" })

    characterData = []
    
    for row in castList.findAll("tr"):
        sections = row.findAll("td")

        ##if the section is populated, then add to character data list
        if len(sections) == 4:
            characterData.append(sections)
            
    return characterData

##given list of scraped data, return list of names
def getNames(characterList):

    actors = []

    ##go through list of characters and get the actor names 
    for character in characterList:
        actor_with_newline = character[1].text

        ##remove newline from the actor name
        actor = removeNewline(actor_with_newline)
        
        actors.append(actor)

    return actors

##given text, remove the newline character
def removeNewline(text):

    cleanText = text.replace("\n","")
    cleanText = cleanText.strip()

    return cleanText
    
##given the url,return tv data
def getTVMovieInfo(url):

    ##list of list of TV data
    ##["Actors", ....]
    TV_data = []
    
    page = scrapePage(url)
    characterData = findFromPage(page)

    TV_data.append(getNames(characterData))

    return TV_data

##given two lists, return the intersection, as a list
def intersection(a,b):

    return list(set(a) & set(b))

##given a list, return the length of the list
def lengthOfList(a):

    return len(a)   

##given a list, return the number of "Fox" 's in the list  
def FoxHunt(names):

    foxes = 0
    
    ##run through the list
    for name in names:

        ##if "Fox" is in the name then add to foxes
        if name.endswith(" Fox"):
            foxes = foxes + 1

    
    return foxes

##given a list, return the names of "Fox" 's in the list
def FoxHuntNames(names):

    foxNames = []
    
    ##run through the list
    for name in names:

        ##if "Fox" is in the name then add to foxes
        if name.endswith(" Fox"):
            foxNames.append(name)

    
    return foxNames

############
### TESTS ##
############
        
####Death in Paradise
##deathInParadiseData = getTVMovieInfo("https://www.imdb.com/title/tt1888075/fullcredits?ref_=tt_cl_sm#cast")
##print(deathInParadiseData[0][3])

####Lewis
##lewisData = getTVMovieInfo("https://www.imdb.com/title/tt0874608/fullcredits?ref_=tt_cl_sm#cast")
##print(lewisData[0][3])

##Foyles's War
##foylesWarData = getTVMovieInfo("https://www.imdb.com/title/tt0310455/fullcredits?ref_=tt_cl_sm#cast")
##print(foylesWarData[0][1])

####Morse
##morseData = getTVMovieInfo("https://www.imdb.com/title/tt0092379/fullcredits/?ref_=tt_ov_st_sm")
##print(morseData[0][1])

####Father Brown
##fatherBrownData = getTVMovieInfo("https://www.imdb.com/title/tt2215842/fullcredits/?ref_=tt_ov_st_sm")
##print(fatherBrownData[0][3])

####Midsomer Murders
##midsomerMurdersData = getTVMovieInfo("https://www.imdb.com/title/tt0118401/fullcredits/?ref_=tt_ov_st_sm")
##print(midsomerMurdersData[0][0])

##print(FoxHunt(lewisData[0]))

####Schindlers List
##schindlersListData = getTVMovieInfo("https://www.imdb.com/title/tt0108052/fullcredits?ref_=tt_cl_sm#cast")
##print(schindlersListData[0][1])

##A New Hope
##aNewHopeData = getTVMovieInfo("https://www.imdb.com/title/tt0076759/fullcredits/?ref_=tt_ov_st_sm")
##print(aNewHopeData[0][1])

##Raiders of the Lost Ark
##raidersData = getTVMovieInfo("https://www.imdb.com/title/tt0082971/fullcredits/?ref_=tt_ov_st_sm")
##print(raidersData[0][1])

##raidersNewHope = intersection(aNewHopeData[0],raidersData[0])
##print(lengthOfList(raidersNewHope))
##print(raidersNewHope)



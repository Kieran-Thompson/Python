##Kieran Thompson

import tkinter as tk
from TVEngine import *
from datalogger import *

tv_movies = {
    "Death in Paradise":"https://www.imdb.com/title/tt1888075/fullcredits?ref_=tt_cl_sm#cast",
    "Lewis":"https://www.imdb.com/title/tt0874608/fullcredits?ref_=tt_cl_sm#cast",
    "Foyles's War":"https://www.imdb.com/title/tt0310455/fullcredits?ref_=tt_cl_sm#cast",
    "Morse":"https://www.imdb.com/title/tt0092379/fullcredits/?ref_=tt_ov_st_sm",
    "Midsomer Murders":"https://www.imdb.com/title/tt0118401/fullcredits/?ref_=tt_ov_st_sm",
    "Schindlers List":"https://www.imdb.com/title/tt0076759/fullcredits/?ref_=tt_ov_st_sm",
    "Raiders of the Lost Ark":"https://www.imdb.com/title/tt0082971/fullcredits/?ref_=tt_ov_st_sm"
    }




##given the window object, return with altered settings
def windowSettings(window):

    ##set the window size and app title text
    window.geometry('1000x600+0+0')

    window.title("Fox Hunt - A IMDB Scrapper")

    return window

##label fuction, place on screen
def labelADD(window, labeltext, row, col, fontStyle, fontSize):

    app = window
    label = tk.Label(app, text=labeltext, font=(fontStyle, fontSize))
    label.grid(row=row, column=col,sticky=tk.W)
    
    return label

##set labels on the screen
def setuplabels(window):

     ##title and description labels
    lbltitle = labelADD(window,"Fox Hunt", 0,0,"Times", 24)
    lblspace = labelADD(window,"",1,0,"Times",13)
    lbldescri = labelADD(window," - A IMDB Scrapper", 2,0,"Times", 16)   

    return window

##setup results frame and widgets 
def resultsFrameSetup(window):


    selectionFrame = tk.Frame(window)
    selectionFrame.grid(row=3,column=0)

    label = tk.Label(selectionFrame, text="TV/Movie List")
    label.pack()

    selectionList = tk.Listbox(selectionFrame,selectmode=tk.SINGLE)
    selectionList.pack(pady=(10,30))

    for item in tv_movies.keys():
        selectionList.insert(tk.END, item)
    

    #########results frame
    resultsFrame = tk.Frame(window,bd=5,relief=tk.GROOVE)
    resultsFrame.grid(row=3,column=1,columnspan=2,padx=30,pady=15)
    

    lblresultsTitle = tk.Label(resultsFrame,text="Results")
    lblresultsTitle.pack(side=tk.TOP)

    ##results window
    results = tk.Text(resultsFrame,cursor="top_side",wrap=tk.WORD,yscrollcommand=set())
    results.insert(tk.INSERT, "Lorem ipsum dolor sit amet.")#####results in here <========
    results.pack(side= tk.LEFT,pady=(0,10))

    ##results button frame
    resultsButtonFrame = tk.Frame(resultsFrame,bd=5,relief=tk.GROOVE)
    resultsButtonFrame.pack(side= tk.RIGHT,padx=(10,30))

    

    ##search function value - selected from a "dropdown button" 
    searchFunction = tk.StringVar(resultsButtonFrame)
    searchFunction.set("FoxHunt")

    
    functions = ["FoxHunt","Fox Count","Cast List","Count"]
    
    ##"dropdown" button
    omSearchFunctions = tk.OptionMenu(resultsButtonFrame, searchFunction,*functions)
    omSearchFunctions.pack( side = tk.TOP)
    
   

    ##search button to run  search IMDB function
    search = tk.Button(resultsButtonFrame, text='Get Results',cursor="draft_large",command= lambda: searchIMDB(searchFunction.get(), results,selectionList))    
    search.pack()

    ##save to CSV file button
    btnSave = tk.Button(resultsButtonFrame, text='Save Results',command= lambda: dataLog(searchFunction.get(),"dsa"))
    btnSave.pack(side = tk.BOTTOM)
    
    return window



##run the search on the given function, return answer to results window
def searchIMDB(searchFunction, results,listbox):

    ##clear results window
    results.delete(1.0,tk.END)
    index = listbox.curselection()
    if index == ():
        index = (0,)
    print(listbox.get(index))
    
    TVMovie = getTVMovieInfo(tv_movies[listbox.get(index)])
    CastList = TVMovie[0]
    
    if searchFunction == "FoxHunt":
        CastList = FoxHuntNames(CastList)
    elif searchFunction == "Fox Count":
        CastList = FoxHunt(CastList)
    elif searchFunction == "Count":
        CastList = lengthOfList(CastList)
    
    
    ##place results in the window
    results.insert(tk.INSERT, str(CastList))


##run the main application
def main():

    print("loading...")

    ##create the main tkinter object 
    window = tk.Tk()
   
    
    ##set the window to correct settings
    window = windowSettings(window)

    ##setup labels 
    window = setuplabels(window)

    ##setup results frame
    window = resultsFrameSetup(window)
    




    
      
    ##run the window object 
    window.mainloop()

    


main()

##Kieran Thompson  15/07/18

import tkinter as tk
from tkinter import messagebox
import EcoScrape
import pyautogui
from twitterScript import *


##given the window object, return with altered settings
def windowSettings(window):

    ##set the window size and app title text
    window.geometry('1200x500+0+0')
    window.title("Economics")

    window.resizable(False, False)

    return window

##create and return a label
def setBasicLabel(window, text_val, col_val, row_val):

    ##set the text, position in the grid and the alignment 
    labelObj = tk.Label(window, text=text_val)
    labelObj.grid(column=col_val, row=row_val, sticky=tk.W)    

    return labelObj

##screenshot the active window
def screenShot(window):

    ## create a screenShot image 
    im = pyautogui.screenshot(region=(window.winfo_x() + 15, window.winfo_y() + 150, 760, 270))

    im.save('screenshot-figures.png')

    ##post to twitter
    twitterMain()

##given the window, place the economic indicators on the screen
def indicators(window):

    ##get the value of CPIH and place on screen as a label
    cpih_text = EcoScrape.getDataFromWeb("https://www.ons.gov.uk/economy/inflationandpriceindices","p","stand-out")[1:-3]
    lblCPIHValue = setBasicLabel(window, "The value of CPIH is " + cpih_text + "%", 0, 2)


    btn_screeenShot = tk.Button(window, text =" Screenshot and Post ", command = lambda: screenShot(window))
    btn_screeenShot.grid(column=1, row=2)


    ##get the value of the Interest rate, place on screen as a label
    interestRate_text = EcoScrape.getDataFromWeb("https://www.bankofengland.co.uk/boeapps/database/Bank-Rate.asp","p","stat-figure")
    lblIRValue = setBasicLabel(window,"The interest rate is " + interestRate_text , 0, 3)


    ##get unemployment value from the web
    unemployment_text = EcoScrape.getDataFromWeb("https://www.ons.gov.uk/employmentandlabourmarket/peoplenotinwork/unemployment","p","stand-out")[1:-3]
    lbl_UE_RateValue = setBasicLabel(window,"The unemployment rate is " + unemployment_text + " %" , 0, 4)



##run the main application
def main():

    print("loading...")

    ##create the tkinter object 
    window = tk.Tk()
    
    ##set the window to correct settings
    window = windowSettings(window)

    ##create a set of labels on screen
    title = setBasicLabel(window,"Below are some important Economic indicators!!", 0, 0)
    space = setBasicLabel(window,"", 0, 1)

    indicators(window)

    space = setBasicLabel(window,"", 0, 7)
    note = setBasicLabel(window,"! - Please take down a note of these economic indicators.   ",0,8)
    

    
    ##run the window object 
    window.mainloop()

main()

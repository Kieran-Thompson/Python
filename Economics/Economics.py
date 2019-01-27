##Kieran Thompson  15/07/18

import tkinter as tk
from tkinter import messagebox
import EcoScrape
import pyautogui
from twitterScript import *




##given the window object, return with altered settings
def windowSettings(window):

    ##set the window size and app title text
    window.geometry('1100x500+0+0')
    window.title("Economics")

    return window

##create and return a label
def setBasicLabel(window, text_val, col_val, row_val):

    ##set the text, position in the grid and the alignment 
    labelObj = tk.Label(window, text=text_val)
    labelObj.grid(column=col_val, row=row_val, sticky=tk.W)    

    return labelObj

##screenshot the active window
def screenShot():

    ##simulate the keypress, up and down  
    im = pyautogui.screenshot(region=(10,150, 580, 270))

    im.save('screenshot.png')

    ##post to twitter
    twitterMain()


##given the window, place the economic indicators on the screen
def indicators(window):

    ##get the value of CPI place on screen as a label
    cpi_text = EcoScrape.getDataFromWeb("https://www.bankofengland.co.uk/monetary-policy/inflation","p","stat-figure")
    lblCPIValue = setBasicLabel(window,"The value of CPI is : " + cpi_text , 0, 2)
    

    btn_screeenShot = tk.Button(window, text =" Screenshot and Post ", command = screenShot)
    btn_screeenShot.grid(column=1, row=2)


    
    ##get the value of the Interest rate, place on screen as a label
    interestRate_text = EcoScrape.getDataFromWeb("https://www.bankofengland.co.uk/monetary-policy/the-interest-rate-bank-rate","p","stat-figure")
    lblIRValue = setBasicLabel(window,"The interest rate is : " + interestRate_text , 0, 3)
   

    ##get unemployment value from the web
    ##second value in the retrived list
    unemployment_text = EcoScrape.getDataFromWeb("https://www.ons.gov.uk/employmentandlabourmarket/peoplenotinwork/unemployment","p","stand-out")[1]
    lbl_UE_RateValue = setBasicLabel(window,"The unemployment rate is : " + unemployment_text + " %" , 0, 4)
    
        
    ##get the value of economic growth value from the web
    economicGrowth_paragraph = EcoScrape.getDataFromWeb("https://en.wikipedia.org/wiki/Economy_of_the_United_Kingdom","div","plainlist")
    

    ##create list and get the value, second value
    economicGrowthList = economicGrowth_paragraph.split(" ")
    lblEGrowth = setBasicLabel(window,"The rate of economic growth is: " + economicGrowthList[1], 0, 5)




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
    note = setBasicLabel(window,"! - Please take down a note of these economic indicators. ",0,8)
    
    ##run the window object 
    window.mainloop()


main()

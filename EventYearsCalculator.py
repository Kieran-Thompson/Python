## 14/06/18
##World Cup Years Calculator

##display the title of the program on screen 
def title():

    ##print title messages
    print("Event Years Calculator")
    print("==========================")
    print()
    print("This calculator will work out if an entered year is a ")
    print("Rugby World Cup, for example or not")
    print()
    print()

##to take input of a year, returning the year if valid 
def takeInput():
    ##take a year as input
    year = input("Please enter a year (YYYY): ")

    ##if the year is valid, return the year
    if validYear(year) == True:
        return year
    else:
        return 0000

##check if the year is a valid input, return True      
def validYear(year):
    
    ##valid length check
    if len(year) != 4:
        print("Invlaid year, incorrect lenght")
        return False
    ##check type
    if year.isdigit() == False:
        print("Invlaid year, incorrect characters")
        return False
    ##check for world wars
    if int(year) < 1948 and int(year) > 1938:
        print("WWII cancelled lots of events in this period")
        return False

    ##if year passes all checks, return True
    return True
    
##calculate if, for example a world cup, happend/should happen, or not. 
def calculate(year):
    ##store the starting years of the events
    ##more events can be added into this dictionary
    startingYears = { 1987:"rugby_WC", 1896:"Summer Olympic", 1930:"football_WC"}

    

    offsets_list = []

    ##workout the offsets for each of the events 
    for eventStartYear in startingYears:
        eventOffset = year - eventStartYear
        offsets_list.append(eventOffset)
        
    events = 0

    ##check if the event falls in mulitples of four after the starting year 
    
    for offset in offsets_list:
        

        ##check the the date is not before the start date
        if offset >= 0:
            if offset % 4 == 0 or offset == 0:
                events = events + 1
                startYear = year-offset                
                displayEvent(year, startingYears[startYear])
                
    if events ==0:
           displayEvent(year, "no event") 

##function to print a message to the screen
##with the correct result shown
def displayEvent(year, event):
    print(str(year) + ", is a " + event + " year")
        

##control the main flow of the program, calling the subroutines 
def main():

    ##call the needed subs and functions
    title()

    while(True):
        year = takeInput()

        if year != 0000:
            calculate(int(year))
            print()
   

##run Program

main()





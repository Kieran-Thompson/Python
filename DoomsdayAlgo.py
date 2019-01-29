###Kieran Thompson
##
##used below source to learn about how it works
###https://www.maplesoft.com/support/help/maple/view.aspx?path=MathApps/DoomsdayAlgorithm




class date:
    '''
    Date class

    Contains the atomic data for a day
    '''

    
      
    ##days dictionary
    ##map numbers to days of the week 
    days = {0:"Sun",1:"Mon",2:"Tues",3:"Wednes",4:"Thrus",5:"Fri",6:"Satur"}

    
    def __init__(self):
        '''
        Constructor method

        Set intial values of the object, when its created
        '''
        self.__dd = None
        self.__mm = self.setMonth()
        self.__yyyy = 4
        self.__leap = self.calculateLeapYear()
        self.__dayOfWeek = None
        

    #Define getters
    def getDay(self):
        ''' return int, dd '''
        return self.__dd
    def getMonth(self):
        ''' return int, mm '''
        return self.__mm
    def getYear(self):
        ''' return int, yyyy '''
        return self.__yyyy
    def isLeapYear(self):
        '''return bool, is leap '''
        return self.__leap
    def getDayOfWeek(self):
        '''return day of the week attribute '''
        return self.__dayOfWeek

    ###day
    def setMonth(self):
        ''' return number, for the date month attribute '''
        notValid = True
        inputMonth=0
        while(notValid):
            
            try:
                inputMonth = int(input("Enter month:"))
                notValid = not(self.checkInRange(1,12,inputMonth))
            except:
                print("Error") 
        return inputMonth
        
    def checkInRange(self,lower,upper,x):
        '''Given range and value, return boolean if value is in the inclusive range '''
        
        if x >= lower and x <= upper:
            return True
        print("Error")
        return False
    

    
    def calculateLeapYear(self):
        if self.getDay() == 4:
            return True
        else:
            return False


    
def main():
    day1 = date()
    print("month " + str(day1.getMonth()))
    
    

##Run code
main()



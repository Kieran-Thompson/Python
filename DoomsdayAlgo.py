###Kieran Thompson
##
##used below source to learn about how it works
###https://www.maplesoft.com/support/help/maple/view.aspx?path=MathApps/DoomsdayAlgorithm



###class containing date information
class date:
      
    ##days dictionary
    ##map numbers to days of the week 
    days = {0:"Sun",1:"Mon",2:"Tues",3:"Wednes",4:"Thrus",5:"Fri",6:"Satur"}

    
    def __init__(self,dd,mm,yyyy):
        self.__dd = dd
        self.__mm = mm
        self.__yyyy = yyyy
        self.__leap = self.calculateLeapYear()
        self.__dayOfWeek = None
        

    ##define getters
    def getDay(self):
        return self.__dd
    def getMonth(self):
        return self.__mm
    def getYear(self):
        return self.__yyyy
    def isLeapYear(self):
        return self.__leap
    def getDayOfWeek(self):
        return self.__dayOfWeek


    ###needs work

    ###multiple of 4 and not of 100
    def calculateLeapYear(self):
        if self.getDay() == 4:
            return True
        else:
            return False


    

day1=date(45,44,2222)
print(day1.getDay())
print(day1.getMonth())
print(day1.getYear())
print(day1.isLeapYear())
print(day1.getDayOfWeek())



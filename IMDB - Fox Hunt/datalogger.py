

import datetime


###for adding to a datalog
def dataLog(date, time, typeOfdetection):


    #set filename to the csv datalogger file and open it
    filename = "datalog.csv"  
    csv_log = open(filename, "a+")


    #create the entry string to put into the csv file 
    row = "Date: " + date + "," +" Time: " + time + "," + "Detection Method: " +  typeOfdetection

    ##write to the file
    csv_log.write(row + "\n")



    csv_log.close()

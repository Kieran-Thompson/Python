

import datetime


###for adding to a datalog
def dataLog(typeOfdetection, data):


    #set filename to the csv datalogger file and open it
    filename = "datalog.csv"  
    csv_log = open(filename, "a+")

    date = datetime.datetime.now()
	
    #create the entry string to put into the csv file 
    row = "Detection Method: " +  typeOfdetection + "," + "Data: " + data

    ##write to the file
    csv_log.write(row + "\n")



    csv_log.close()

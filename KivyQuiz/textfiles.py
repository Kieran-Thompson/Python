##Kieran Thompson

class downloadStack():
    """ A class to store items as a stack, to a textfile """

    def __init__(self, filename):
        """ Create a stack object 
        
        This includes a filename and size

        self._filename - the file used as the stack storage
        self._fileSize - the pointer used to get the object from the stack

        """

        self._filename = filename + ".txt"
        self._fileSize = self.readAllFile()

    def getFileSize(self):
        """Get the size of the file, 
        in terms of the number of items in it 
        """

        return self._fileSize

    def increaseFileSize(self, numberOfItems):
        """ Increase the file size by a given number """

        self._fileSize = self._fileSize + numberOfItems
        return self._fileSize

    def decreaseFileSize(self, numberOfItems):
        """ Reduce the file size by a given number """

        if self._fileSize == 0:
            return 0
        self._fileSize = self._fileSize - numberOfItems
        return self._fileSize


    def saveItem(self, itemBlock):
        """Save items to the file """

        file = open(self._filename,"a+")
        file.write("%s\n" % str((itemBlock)))
        self.increaseFileSize(1)
        file.close()

    def getItem(self):
        file = open(self._filename, "r+")
        count = self.getFileSize()
        itemList = []
        for item in file:
            itemList.append(item)
        file.close()


        print(itemList)

        lastItem = itemList[-1]
        itemList.pop()


        print(itemList)


        file = open(self._filename,"w+")
        for item in itemList:
            file.write(item)
        file.close()


        print(lastItem)
        print(type(lastItem))
        return lastItem
        

    def readAllFile(self):
        """ Get the stack pointer, by getting the size of the stack"""

        ##Try to step through the stack  textfile, and count the lines
        try:
            file = open(self._filename, "r")
            count = 0
            for x in file:
               count = count + 1
            file.close()

        ##If error then set the pointer to 0
        except:
            count = 0

        return count


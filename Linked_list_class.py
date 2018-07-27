##Kieran Thompson  19/01/18
##Linked List Stuff


## Node class - contains data item and link to next node
class node:

    ##create node
    def __init__(self, data):
        self._next = None
        self._data = data

    ##getter function for the data on the node
    def getData(self):
        return self._data

##Linked List class (LL Class)
class linkedList:

    ##create a linked list
    def __init__(self):
        self._head = None

    ##print the list from first to last element
    def printLL(self):
        ##get the head of the LL
        currentNode = self._head

        ##until the next one is not none, print it and move to the next element 
        while (currentNode != None):
            print(currentNode.getData())
            currentNode = currentNode.next

    ##function to add node to the start of the LL
    def addToStart(self, data):

        ##create a new node with the data
        NodeToBeAdded = node(data)

        ## make the node point to the old head of the LL
        NodeToBeAdded.next = self._head

        ##make the new head of the LL, the new head
        self._head = NodeToBeAdded

####things to add to this 
### add to middle
### add to end



##code
def createLL():
    newLL = linkedList()
    return newLL

def runAddToLL():
    LL = linkedList()

    print("ADD TO START TEST")
    ##add to LL at the start 
    LL.addToStart("Second")
    LL.addToStart("First")
    LL.printLL()

    
runAddToLL()






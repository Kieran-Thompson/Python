##Kieran Thompson  19/01/18
##Linked List Stuff


## Node class - contains data item and link to next node
class node:

    ##create node
    def __init__(self, data):
        self.next = None
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

        ##until the node is not none, print it and move to the next element 
        while (currentNode):
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

    ##add nodes at the end of the LL
    def addToEnd(self, data):

        ##create the node
        nodeToAdd = node(data)      

        ##run through the linked list to the end
        currentNode = self._head
        while (currentNode.next):
            currentNode = currentNode.next
            
        ##add the node to the lined list
        currentNode.next = nodeToAdd
        
        

####things to add to this 
### add to middle


def runAddToLL():
    LL = linkedList()

    ##add to LL at the start 
    print("ADD TO START TEST")
    
    LL.addToStart("Two")
    LL.addToStart("One")
    LL.addToStart("Zero")
    LL.printLL()
    print()
    
    ##add to LL at the end
    print("ADD TO END TEST")
    
    LL.addToEnd("Three")
    LL.addToEnd("Four")
    LL.printLL()

    

    
runAddToLL()






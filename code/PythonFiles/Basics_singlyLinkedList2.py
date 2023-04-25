# defining the Node
class Node:
    def __init__(self):      #constructor
        self.data=None
        self.Next=None
    def setData(self,Data):   #getting data
        self.data=Data
    def getData(self):        #fetching data
        return self.data
    def setNext(self,Next):   #setting Next
        self.Next=Next
    def getNext(self):        #fetching Next  
        return self.Next
    def hasNext(self):        #to check for the last Node
        return self.Next!=None


# Linked-list
class linked_list:
    def __init__(self):
        self.head=None
        self.length=0
# Printing the list data 
    def listlength(self):
        current = self.head
        count = 0
        while current!=None:
            count = count + 1
            current = current.getNext()
        return count
# Inserting Node at the beginning
    def insertAtBeginning(self,data):
        newNode = Node()
        newNode.setData(data)
    
        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head=newNode
        self.length+=1
# Inserting at the end
    def insertAtEnd(self,data):
        newNode=Node()
        newNode.setData(data)
        current = self.head
        while current.getNext()!=None:
            current = current.getNext()
        
            current.setNext(newNode)
            self.length+=1

            # Inserting at any position in the list
    def insertAtPos(self,pos,data):
        if pos < 0 or pos > self.length:
            print ('Wrong position')
            return None
        else:
            if pos ==0:
                self.insertAtBeginning(data)
            else:
                if pos == self.length:
                    self.insertAtEnd(data)
                else:
                    newNode = Node()
                    newNode.setData(data)
                    count = 0
                    current = self.head
                    while count < pos-1:
                        count+=1
                        current = current.getNext()
                    newNode.setNext(current.getNext())
                    current.setNext(newNode)
                    self.length+=1
# deleting the first Node
    def delfromBeg(self):
        if self.length==0:
            print ("the list is empty")
        else:
            self.head = self.head.getNext()
            self.length-=1
# deleting the last Node 
    def delfromlast(self):
        if self.length == 0:
            print ("the list is empty")
        else:
            current = self.head
            previous = self.head
            while current.getNext()!=None:
                previous = current
                current = current.getNext()
            previous.setNext(None)
            self.length-=1
# deleting intermediate Node
    
    def delintermediate(self,Node):
        if self.length == 0:
            print ("list is alredy empty")
        else:
            current = self.head
            found = False
            while not found:
                if current == Node:
                    found = True
                #elif current is None:
                 #   print "Node not in the list"
                else:
                    previous = current
                    current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            self.length-=1
    def search( self, k ) :
        p = self.head
        if p != None :
            while p.getNext() != None :
                if ( p.getData() == k ) :
                    return p
                p = p.getNext()
            if ( p.getData() == k ) :
                return p
    
    def __str__(self):
        s = ""
        current = self.head
        if current != None:
            
            while current:
                s = s + current.getData() + str('->')
                current = current.getNext()    
        return s[:-2]
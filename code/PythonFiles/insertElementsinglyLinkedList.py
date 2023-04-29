class Node:
    def __init__(self) -> None:
        self.data = None
        self.next = None
    def getData(self): return self.data

    def setData(self,Data):
        self.data = Data
    
    def getNext(self):return self.next

    def setNext(self,Next): 
        self.next = Next

    def hasNext(self):
        return self.next!=None

class LinkedList:
    def __init__(self) -> None:
        self.head =  None
        self.length = None
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    def insertAtBegining(self,Data):
        newNode = Node()
        newNode.setData(Data)
        if self.length ==0 :
            newNode = self.head
            self.length+=1
        else:
            newNode.setNext(self.head)
            # we have set new node pointing towards current linked list head and now will set self.head pointer to point the current newNode 
            self.head = newNode
            self+=1
        
    def insertAtEnd(self,Data):
        newNode =  Node()
        newNode.setData(Data)
        if self.length == 0:
            newNode = self.head
            self.length+=1
        else:
            currenthead = self.head
            while currenthead.getNext():
                currenthead = currenthead.getNext()
            currenthead.setNext(newNode)
            self.length+=1

    # def insertAtPos(self,data):

llobj = LinkedList()


    
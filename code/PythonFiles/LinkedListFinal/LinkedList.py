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
        self.length = 0
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    def insertAtBegining(self,Data):
        newNode = Node()
        newNode.setData(Data)
        if self.length == 0 :
            self.head= newNode
            self.length += 1
        else:
            newNode.setNext(self.head)
            self.head = newNode
            self.length+=1
        
    def insertAtEnd(self,Data):
        newNode =  Node()
        newNode.setData(Data)
        if self.length == 0:
            newNode = self.head
            self.length+=1
        else:
            currenthead = self.head
            while currenthead.hasNext():
                currenthead = currenthead.getNext()
            currenthead.setNext(newNode)
            self.length+=1

    def insertAtPos(self,Data,pos):
        newNode = Node()
        newNode.setData(Data)
        err_ = "loc index out of bound"
        if self.length < pos or pos < 0  : 
            print(err_)
        elif pos == 0:
            self.insertAtBegining(Data)
            self.length+=1
        elif pos == self.length:
            self.insertAtEnd(Data)
            self.length+=1
        else:
            currentPointer = self.head 
            count = 0
            while count < pos-1:
               count+=1
               currentPointer = currentPointer.getNext()
            newNode.setNext(currentPointer.getNext())
            currentPointer.setNext(newNode)
            self.length+=1
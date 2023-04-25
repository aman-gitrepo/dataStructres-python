class Node:
    # constructor to initialize Node
    def __init__(self):
        self.data = None
        self.next = None 

    def setData(self,Data):
        self.data = Data
    def getData(self):
        return self.data
    
    def setNext(self,Next):
        self.next = Next
    def getNext(self):
        return self.next
    
    def hasNext(self):
        return self.next!=None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def listLength(self):
        current =  self.head
        count = 0
        while current:
            count = count + 1
            current = current.next
        print(count)
    
    def printlist(self):
        current =  self.head
        final = []
        while current:
            final = final.append(current.data)
            current = current.next
        return final
    
    def insertAtBeginning(self,data):
        newNode = Node()
        newNode.setData(data)
    
        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head=newNode
        self.length+=1
    
    def insertAtEnd(self,data):
        newNode=Node()
        newNode.setData(data)
        current = self.head
        while current.getNext()!=None:
            current = current.getNext()
            current.setNext(newNode)
            self.length+=1

llist = LinkedList()
llist.insertAtBeginning('aman1')
llist.insertAtBeginning('aman2')
llist.insertAtBeginning('aman3')


llist.listLength()
llist.printlist()

# print ([node.data for node in llist])
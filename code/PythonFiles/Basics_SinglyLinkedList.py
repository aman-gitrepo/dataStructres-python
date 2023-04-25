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
        outarr = [current.data]
        while current.next:
            current = current.next
            outarr.append(current.data)
        return outarr
    
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
        currentNode = self.head
        while currentNode.next != None :
            currentNode = currentNode.next
        currentNode.next = newNode
        self.length+=1

llist = LinkedList()
llist.insertAtBeginning('aman1')
llist.insertAtBeginning('aman2')
llist.insertAtBeginning('aman3')
llist.insertAtEnd('end0')
llist.insertAtEnd('end1')
llist.insertAtEnd('end2')

llist.listLength()
print(llist.printlist())

print ([node.data for node in llist])

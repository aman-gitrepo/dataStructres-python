class Node:
    def __init__(self, Data = None, prev = None , next = None):
        self.data = Data
        self.prev = prev
        self.next = next
    
    def setData(self , Data):
        self.data = Data

    def setNext(self , next):
        self.next = next

    def setPrev(self , prev):
        self.prev = prev
    
    def getNext(self):
        return self.next
    
    def getData(self):
        return self.data
    
    def getPrev(self):
        return self.prev
    
    def hasNext(self):
        return self.next!=None
    
    def hasPrev(self):
        return self.prev!=None


class DoublyLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def getNode(self,index):
        currentNode = self.head
        if currentNode == None:
            return None
        currentIndex =  0
        while currentIndex < index :
            currentNode = currentNode.next
            currentIndex+=1
        return currentNode
        # return currentNode.getData()


    def insertAtBegining(self , data):
        newNode = Node()
        newNode.setData(data)
        if self.head == None:
            self.head = self.tail = newNode
            print('set head and tail as newNode')
            self.length+=1
        else:
            current = self.head
            newNode.next = current
            newNode.prev = None
            current.prev = newNode
            self.head = newNode
            self.length+=1
    
    def insertAtEnd(self,data):
        newNode = Node()
        newNode.setData(data)
        if self.head == None:
            self.head = self.tail = newNode
            print('set head and tail as newNode')
            self.length+=1
        else:
            current =  self.head
            while current.hasNext():
                current =  current.getNext()
            current.next = newNode
            newNode.prev = current
            newNode.next = None
            self.tail = newNode
            self.length+=1

    def insertAtPos(self,data,pos):
        newNode = Node()
        newNode.setData(data)
        if pos <0 or pos > self.length:
            return ValueError('this is invalid position')
        elif pos == 0 :
            self.insertAtBegining(data)
            self.length+=1
        elif pos == self.length-1:
            self.insertAtEnd(data)
            self.length+=1
        else:
            current  = self.head 
            currentIndex = 0
            while currentIndex < pos-1:
                current = current.next
                currentIndex+=1
            # print(current.getData())
            nextToCurrent = current.getNext()
            nextToCurrent.setPrev(newNode)
            newNode.prev  = current
            newNode.next = current.next
            current.next = newNode
            # print(nextToCurrent.getPrev().data)

    def deleteAtIndex(self,index):
        headNode = self.head
        tailNode = self.tail
        secondToTailNode = tailNode.prev
        if index <0 and index>self.length:
            return ValueError('errored cause ofindex not present')
        elif index ==0:
            self.head = self.head.next
            self.length-=1
        elif index == self.length-1:
            tailNode.prev = None
            secondToTailNode.next = None
            self.tail = secondToTailNode
            self.length-=1
        else:
            currentIndex = 1
            while currentIndex <= index :
                currentIndex += 1
                headNode = headNode.next
            headNode.prev.next = headNode.next
            self.length-=1


new = DoublyLinkedList()
new.insertAtBegining(1)
new.insertAtBegining(10)
new.insertAtBegining(100)
new.insertAtBegining(1000)
new.insertAtEnd(1000)
ll = [x.data for x in new]
print(ll)
# print(new.getNode(1).getData())
new.insertAtPos('testInsert',2)
print(new.getNode(2).getData())
ll = [x.data for x in new]
print(ll)
new.deleteAtIndex(new.length)
ll = [x.data for x in new]
print(ll)
new.deleteAtIndex(new.length)
ll = [x.data for x in new]
print(ll)
new.deleteAtIndex(new.length)
ll = [x.data for x in new]
print(ll)
new.deleteAtIndex(new.length)
ll = [x.data for x in new]
print(ll)
new.deleteAtIndex(new.length)
ll = [x.data for x in new]
print(ll)
class Node():
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self,Data):self.data = Data
    def getData(self):return self.data
    def setNext(self,Next):self.next = Next
    def getNext(self):return self.next
    def hasNext(self):return self.next!=None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        start = self.head
        while start:
            yield start
            start = start.next

    def appendToLinkList(self,data):
        if self.length==0:
            newNode=Node()
            newNode.setData(data)
            self.head = newNode
            self.length+=1
        else:
            newNode=Node()
            newNode.setData(data)
            headNode = self.head
            while headNode.next != None :
                headNode = headNode.next
            headNode.setNext(newNode)

ll = LinkedList()
ll.appendToLinkList('1')
ll.appendToLinkList('2')
ll.appendToLinkList('3')
ll.appendToLinkList('4')

print([x.data  for x in ll])

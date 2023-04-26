class Node():
    def __init__(self):
        self.data = None
        self.next = None
        
    def setData(self, Data):self.data = Data
    def getData(self):return self.data

    def setNext(self,Next): self.next = Next
    def getNext(self):return self.next

    def hasNext(self):
        return self.next!=None

class SinglyLinkedList():
    def __init__(self) -> None:
        self.length = 0
        self.head = None

    def __iter__(self):
        startNode = self.head
        while startNode:
            yield startNode
            startNode =  startNode.getNext()

    def add(self,data):
        if self.length == 0:
            print('input -------------->'+data)
            newNode = Node()
            newNode.setData(data)
            self.head =  newNode
            self.length+=1
        else:
            print('input -------------->'+data)
            newNode = Node()
            newNode.setData(data)
            headNode = self.head
            while headNode.next != None :
                headNode = headNode.next
            headNode.next = newNode
            print('stored value at {} is {}'.format(headNode.next , headNode.next.data))
            self.length+=1
        print('currentLinked list length is '+str(self.length))

ll = SinglyLinkedList()
ll.add('1')
ll.add('2')
ll.add('3')
ll.add('4')
ll.add('5')
print([x.data  for x in ll])


# input -------------->1
# currentLinked list length is 1
# input -------------->2
# stored value at <__main__.Node object at 0x0000025A10B065D0> is 2
# currentLinked list length is 2
# input -------------->3
# stored value at <__main__.Node object at 0x0000025A10B140D0> is 3
# currentLinked list length is 3
# input -------------->4
# stored value at <__main__.Node object at 0x0000025A10B14110> is 4
# currentLinked list length is 4
# input -------------->5
# stored value at <__main__.Node object at 0x0000025A10B14150> is 5
# currentLinked list length is 5
# ['1', '2', '3', '4', '5']
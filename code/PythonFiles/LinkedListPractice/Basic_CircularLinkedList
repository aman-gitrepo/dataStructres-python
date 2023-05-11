class Node:
    def __init__(self):
        self.data = None
        self.next = None

class cLinkedList:
    def __init__(self):
        self.length = 0
        self.tail   = None
        self.head   = None

    def insertAtBegining(self,data):
        node = Node()
        node.data = data
        headNode = self.head
        if self.head == None:
            node.next = headNode
            self.head = self.tail = node
        else:
            node.next = headNode
            self.head = node
            self.tail.next = self.head
        self.length+=1
    
    def insertAtEnd(self,data):
        node = Node()
        node.data = data
        nxhNode = self.head.next
        if self.tail ==None:
            self.head = self.tail = node
            print('out')
        else:
            while nxhNode!=self.head:
                print('in')
                nxhNode = nxhNode.next
            print(nxhNode.data) 
            nxhNode.next = node
            self.tail = node
            node.next = self.head
        self.length+=1


    
ccl= cLinkedList()
ccl.insertAtBegining(1)
ccl.insertAtBegining(11)
ccl.insertAtBegining(111)
ccl.insertAtBegining(1111)
ccl.insertAtBegining(11111)
ccl.insertAtEnd(10)
ccl.insertAtBegining(0)
print(ccl.head.data)
print(ccl.tail.data)
print(ccl.tail.next.data)
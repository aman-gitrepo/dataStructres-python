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
            return None
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

    def delAtBegin(self):
        if self.length == 0:
            print('LinkedList is empty')
            return None
        current = self.head
        self.head = current.next
        self.length-=1

    def delAtEnd(self):
        if self.length == 0:
            return None
        else:
            current = self.head
            count = 1
            while count < self.length-1:
                count+=1
                current = current.next
            current.setNext(None)
            self.length-=1
    
    def deleteFromLinkedListwithNode(self,node):
        if self.length ==0:
            raise ValueError('linkedList is Empty')
        else:
            current = self.head
            previous = None
            found =  False

            while not found:
                if current == node:
                    found = True
                elif current is None:
                    raise ValueError('Node not in linked list')
                else:
                    previous = current
                    current  = current.next
        if previous is None:
            self.head = current.next 
        else:
            previous = current.next
        self.length-=1
    
    def deleteWithValue(self,data):
        currentnode = self.head
        previousnode = self.head
        while currentnode.next!=None or currentnode.data != data:
            if currentnode.data == data:
                previousnode =  currentnode.next
                self.length -=1
                return
            else:
                previousnode = currentnode
                currentnode = currentnode.next
            print('value provided is not present')

    def deleteAtPos(self,pos):
        count = 0
        currentnode = self.head
        previousnode = self.head
        print(pos, 'to be deleted')
        ll1 = [ x.data for x in self]
        if ll1:
            print(ll1, 'is linked list befor deletion')
        if pos > self.length or pos < 0:
            print('position does not exist within linked list')
        elif pos == 0:
            current = self.head
            self.head = current.next
            self.length-=1
        else:
            print(pos, 'reached if block')
            while currentnode.hasNext() or count <= pos:
                print('count is ', count, 'reached while with pos',pos)
                if count  == pos:
                    print(count, 'in count within while')
                    previousnode.next = currentnode.next
                    currentnode.next = None
                    self.length-=1
                    return
                else:
                    previousnode = currentnode
                    currentnode  = currentnode.next
                count = count+1 

    
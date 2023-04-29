import singlyLinkedList

newLl = singlyLinkedList.LinkedList()

newLl.insertAtBegining(0)
newLl.insertAtBegining(1)
newLl.insertAtBegining(3)
newLl.delAtEnd()

ll = [ x.data for x in newLl]
if ll:
    print(ll)

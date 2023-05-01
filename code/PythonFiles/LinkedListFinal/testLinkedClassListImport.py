import singlyLinkedList

newLl = singlyLinkedList.LinkedList()

newLl.insertAtBegining(0)
newLl.insertAtBegining(1)
newLl.insertAtBegining(3)
newLl.delAtEnd()

new2 = singlyLinkedList.LinkedList()
new2.insertAtBegining(0)
new2.insertAtBegining(1)
new2.insertAtBegining(3)


ll = [ x.data for x in newLl]
if ll:
    print(ll)

ll = [ x.data for x in new2]
if ll:
    print(ll)
import singlyLinkedList

new2 = singlyLinkedList.LinkedList()
new2.insertAtBegining(0)
new2.insertAtBegining(1)
new2.insertAtBegining(2)
new2.insertAtBegining(3)
new2.deleteAtPos(1)

ll1 = [ x.data for x in new2]
if ll1:
    print(ll1)
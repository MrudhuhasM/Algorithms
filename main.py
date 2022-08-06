from lists.linked_list import LinkedList
from lists.circular_linked_list import CircularList

li1 = CircularList()
li1.insertAtBegining(1)
li1.insertAtBegining(2)
li1.insertAtBegining(3)
li1.insertAtBegining(4)
li1.insertAtBegining(5)
li1.insertAtBegining(6)
li1.insertAtBegining(7)
li1.insertAtBegining(8)
li1.insertAtEnd(0)

li1.deleteAtBegining()
li1.deleteAtNode(3)

print("Head",li1.head)
print("Length",li1.length)

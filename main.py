from lists.lists import LinkedList

li1 = LinkedList()
li1.insertAtBegining(1)
li1.insertAtBegining(2)
li1.insertAtEnd(0)

print("Head",li1.head)
print("Length",li1.length)

li1.deleteAtBegining()
li1.deleteAtEnd()
li1.deleteAtNode(4)

print("Head",li1.head)
print("Length",li1.length)
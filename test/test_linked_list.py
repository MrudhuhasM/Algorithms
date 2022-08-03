from lists.lists import LinkedList

def initialize_linkedlist():
    li1 = LinkedList()
    li1.insertAtBegining(1)
    li1.insertAtBegining(2)
    li1.insertAtBegining(3)
    li1.insertAtBegining(4)
    li1.insertAtBegining(5)
    li1.insertAtBegining(6)
    li1.insertAtBegining(7)
    li1.insertAtBegining(8)
    li1.insertAtEnd(0)

    return li1

def test_insertion():
    new_list = initialize_linkedlist()
    new_list.insertAtBegining(9)
    new_list.insertAtEnd(0)
    new_list.insertAtMiddle(4,6)

    assert new_list.head == 9
    assert new_list.length == 12

def test_deletion():
    new_list = initialize_linkedlist()
    new_list.deleteAtBegining()
    new_list.deleteAtEnd()
    new_list.deleteAtNode(3)

    assert new_list.head == 7
    assert new_list.length == 6
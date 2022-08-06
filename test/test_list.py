import unittest
from lists.linked_list import LinkedList
from lists.double_linked_list import DoubleLinkedList
from lists.circular_linked_list import CircularList



def initialize_linkedlist(type):
    li1 = type
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


class TestLinkedList(unittest.TestCase):
    def test_insertion(self):
        new_list = initialize_linkedlist(LinkedList())
        new_list.insertAtBegining(9)
        new_list.insertAtEnd(0)
        new_list.insertAtMiddle(4,6)

        self.assertEqual(new_list.head , 9)
        self.assertEqual(new_list.length,12)


    def test_deletion(self):
        new_list = initialize_linkedlist(LinkedList())
        new_list.deleteAtBegining()
        new_list.deleteAtEnd()
        new_list.deleteAtNode(3)

        self.assertEqual(new_list.head , 7)
        self.assertEqual(new_list.length,6)

class TestDoubleList(unittest.TestCase):
    def test_insertion(self):
        new_list = initialize_linkedlist(DoubleLinkedList())
        new_list.insertAtBegining(9)
        new_list.insertAtEnd(0)
        new_list.insertAtMiddle(4,6)

        self.assertEqual(new_list.head , 9)
        self.assertEqual(new_list.length,12)


    def test_deletion(self):
        new_list = initialize_linkedlist(DoubleLinkedList())
        new_list.deleteAtBegining()
        new_list.deleteAtEnd()
        new_list.deleteAtNode(3)

        self.assertEqual(new_list.head , 7)
        self.assertEqual(new_list.length,6)

class TestCircleList(unittest.TestCase):
    def test_insertion(self):
        new_list = initialize_linkedlist(CircularList())
        new_list.insertAtBegining(9)
        new_list.insertAtEnd(0)
        new_list.insertAtMiddle(4,6)

        self.assertEqual(new_list.head , 9)
        self.assertEqual(new_list.length,12)


    def test_deletion(self):
        new_list = initialize_linkedlist(CircularList())
        new_list.deleteAtBegining()
        new_list.deleteAtEnd()
        new_list.deleteAtNode(3)

        self.assertEqual(new_list.head , 7)
        self.assertEqual(new_list.length,6)
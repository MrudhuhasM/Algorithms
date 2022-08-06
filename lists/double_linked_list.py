from node import Node
from typing import Any

class DoubleLinkedList:
    def __init__(self) -> None:
        self._length =0
        self._head = None
        self._tail = None

    @property
    def head(self):
        return self._head.data

    @head.setter
    def head(self):
        raise TypeError("Not allowed")

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self):
        raise TypeError("Not Allowed")

    def check_list_empty(method)-> None:
        def wrapper_(self):
            if self._length >= 0:
                method(self)
            else:
                raise ValueError("Empty List")
        return wrapper_
    
    def insertAtBegining(self,data: Any) -> None:
        new_node = Node()
        new_node.data = data
        if self._head == None:
            self._head = self._tail = new_node
        else:
            new_node.prev = None
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._length += 1
    
    def insertAtEnd(self,data: Any)-> None:
        new_node = Node()
        new_node.data = data
        if self._head == None:
            self._head = self._tail = new_node
        else:
            current = self._head
            while current.next != None:
                current = current.next
            new_node.prev = current
            new_node.next = None
        self._length += 1
    
    def insertAtMiddle(self,pos: int,data: Any) -> None:
        new_node = Node()
        new_node.data = data
        if pos > self._length or pos < 0:
            raise IndexError("Invalid Position")
        elif self._length == 0:
            self.insertAtbegining(data)
        elif pos == self._length:
            self.insertAtEnd(data)
        else:
            count = 0
            current = self._head
            while count < pos:
                current = current.next
                count += 1
            previous = current.prev
            previous.next = new_node
            new_node.prev = previous
            new_node.next = current
            current.prev = new_node
            self._length += 1
    
    @check_list_empty
    def deleteAtBegining(self)-> None:
        current = self._head
        self._head = current.next
        self._head.prev = None
        self._length -= 1

    @check_list_empty
    def deleteAtEnd(self) -> None:
        if self._length == 1:
            self.deleteAtBegining()
        else:
            current = self._head
            while current.next != None:
                current = current.next
            previous = current.prev
            previous.next = None
            self._length -= 1
    
    def deleteAtNode(self,pos: int) -> None:
        if self._length == 0:
            raise ValueError("Empty list")
        elif self._length == 1:
            self.deleteAtBegining()
        elif self._length == pos:
            self.deleteAtEnd()
        else:
            count = 0
            current = self._head
            while count < pos:
                current = current.next
                count += 1
            previous = current.prev
            current_next = current.next
            previous.next = current_next
            current_next.prev = previous
            self._length -= 1

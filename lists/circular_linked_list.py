from .node import Node
from .lists_abc import ListsABC
from typing import Any

class CircularList(ListsABC):

    def __init__(self) -> None:
        super().__init__()

    def check_list_empty(method)-> None:
        def wrapper_(self):
            if self._length >= 0:
                method(self)
            else:
                raise ValueError("Empty List")
        return wrapper_

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

    def printList(self):
        current = self._head
        if current == 0:
            return 0
        print(current.data)
        current = current.next
        while current != self._head:
            current = current.next
            print(current.data)

    def insertAtBegining(self, data) -> None:
        new_node = Node()
        new_node.data = data
        if self._length > 0:
            current = self._head
            while current.next != self._head:
                current = current.next
            current.next = new_node
            new_node.next = self._head
            self._head = new_node
        else:
            self._head = new_node
            new_node.next = self._head

        self._length += 1

    def insertAtEnd(self, data: Any) -> None:
        new_node = Node()
        new_node.data = data
        if self._length > 0:
            current = self._head
            while current.next != self._head:
                current = current.next
            current.next = new_node
            new_node.next = self._head
            self._length += 1
        else:
            self.insertAtBegining(data)

    def insertAtMiddle(self, pos: int, data: Any) -> None:
        if pos < 0 or pos >= self.length:
            raise IndexError("Position out of bounds")
        elif pos == 0:
            self.insertAtBegining(data)
        elif pos == self._length:
            self.insertAtEnd(data)
        else :
            new_node = Node()
            new_node.data = data
            count = 0
            prev = self._head
            current = self._head
            while count < pos:
                prev = current
                current = current.next
                count += 1
            prev.next = new_node
            new_node.next = current
            self._length += 1
    
    @check_list_empty
    def deleteAtBegining(self) -> None:
        current = self._head
        last = self._head
        while last.next != self._head:
            last = last.next
        last.next = current.next
        self._head = current.next
        self._length -= 1

    @check_list_empty
    def deleteAtEnd(self) -> None:
        current = self._head
        previous = self._head
        while current.next != self._head:
            print(current.data)
            previous = current
            current = current.next
        previous.next = self._head
        self._length -= 1

    def deleteAtNode(self, pos: int) -> None:
        if self._length == 0:
            raise ValueError("Empty list")
        elif self._length == 1:
            self.deleteAtBegining()
        elif self._length == pos:
            self.deleteAtEnd()
        else:
            count = 0
            previous = self._head
            current = self._head
            while count < pos:
                previous = current
                current = current.next
                count += 1
            previous.next = current.next
            self._length -= 1


        
    

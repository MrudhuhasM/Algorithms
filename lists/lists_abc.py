from abc import ABCMeta,abstractmethod
from typing import Any

class ListsABC():
    def __init__(self) -> None:
        self._head = None
        self._length = 0

    @property
    @abstractmethod
    def head(self):pass

    @head.setter
    @abstractmethod
    def head(self):pass

    @property
    @abstractmethod
    def length(self):pass

    @length.setter
    @abstractmethod
    def length(self):pass

    @abstractmethod
    def insertAtBegining(self,data)-> None:pass

    @abstractmethod
    def insertAtEnd(self,data: Any)-> None:pass

    @abstractmethod
    def insertAtMiddle(self,pos: int,data: Any)-> None:pass

    @abstractmethod
    def deleteAtBegining(self)-> None:pass

    @abstractmethod
    def deleteAtEnd(self)-> None:pass

    @abstractmethod
    def deleteAtNode(self,pos: int)-> None:pass


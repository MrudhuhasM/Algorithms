class Node:
    """
    Class representing a node
    """

    def __init__(self) -> None:
        self._data = None
        self._next = None
        self._prev = None

    def check_type(method):
        def wrapper_(self,list_type):
            if list_type == LinkedList():
                raise TypeError('Function not allowed in  linked list')
        return wrapper_

    @property
    def list_type(self):
        return self._list_type

    @list_type.setter
    def list_type(self,list_type):
        self._list_type = list_type
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self,data):
        self._data = data

    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self,next):
        self._next = next

    def hasNext(self):
        return self._next != None

    @property
    @check_type
    def prev(self):
        return self._prev
    
    @prev.setter
    @check_type
    def prev(self,prev):
        self._prev = prev

   
class LinkedList:

    def __init__(self) -> None:
        self._length =0
        self._head = None
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

    def insertAtBegining(self,data):
        new_node = Node()
        new_node.data = data
        new_node.list_type = LinkedList
        if self._length > 0:
            currentnode = self._head
            self._head = new_node
            new_node.next = currentnode
        else:
            self._head = new_node
        self._length += 1

    def insertAtEnd(self,data):
        new_node = Node()
        new_node.data = data
        new_node.list_type = LinkedList
        if self._length > 0:
            currentnode = self._head
            while currentnode.next != None:
                currentnode = currentnode.next
            currentnode.next = new_node
            self._length += 1
        else:
            self.insertAtBegining(data)
    
    def insertAtMiddle(self,pos,data):
        new_node = Node()
        new_node.data = data
        new_node.list_type = LinkedList
        if pos > self._length or pos< 0:
            raise IndexError('Position out of index')
        elif self._length == 0:
            self.insertAtBegining(data)
        elif self._length == pos:
            self.insertAtEnd(data)
        else:
            count = 0
            previousnode = self._head
            currentnode = self._head
            while count < pos:
                previousnode = currentnode
                currentnode  = currentnode.next
                count += 1
            previousnode.next = new_node
            new_node.next = currentnode
            self._length += 1

    def check_list_empty(method):
        def wrapper_(self):
            if self._length >= 0:
                method(self)
            else:
                raise ValueError("Empty List")
        return wrapper_
    
    @check_list_empty
    def deleteAtBegining(self):
        currenthead =self._head
        self._head = currenthead.next
        self._length -=1

    
    @check_list_empty
    def deleteAtEnd(self):
        previoushead = self._head
        currenthead = self._head
        while currenthead.next != None:
            previoushead = currenthead
            currenthead = currenthead.next
        previoushead.next = None
        self._length -= 1        

    
    def deleteAtNode(self,pos):
        if self._length >= 0:
            if pos > self._length or pos < 0:
                raise IndexError("index out of range")
            else:
                count = 0
                currenthead = self._head
                previoushead = self._head
                while count < pos:
                    previoushead = currenthead
                    currenthead = currenthead.next
                    count += 1
                previoushead.next = currenthead.next
                self._length -= 1
        else:
            raise ValueError("Empty List")





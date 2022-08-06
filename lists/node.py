class Node:
    """
    Class representing a node
    """

    def __init__(self) -> None:
        """
        Constructor for Node
        """
        self._data = None
        self._next = None
        self._prev = None

    # def check_type(method):
    #     """
    #     Checks what class a node belongs to so we can diable prev for linked list
    #     """
    #     def wrapper_(self):
    #         if self.list_type == LinkedList():
    #             raise TypeError('Function not allowed in  linked list')
    #     return wrapper_

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
    def prev(self):
        return self._prev
    
    @prev.setter
    def prev(self,prev):
        self._prev = prev

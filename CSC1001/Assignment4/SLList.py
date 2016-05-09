class Node:
    """
    The Class of a Node in a singly connect list.
    """

    def __init__(self, element, pointer):
        self.element = element
        self.pointer = pointer


class SLList:
    """
    The Class of a Singly Connected List
    Forked from teacher
    """

    def __init__(self):
        """
        Initializing with the reference of head and tail as None
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        """
        :return: The length of the list.
        """
        return self.size

    def is_empty(self):
        """
        Check if the length = 0
        :return:
        """
        return self.size == 0

    def insert_head(self, e):
        """
        Add a node in the front of a list.
        :param e:
        :return:
        """
        newest = Node(e, None)
        newest.pointer = self.head
        self.head = newest
        if self.is_empty():
            self.tail = newest
        self.size += 1
        return newest

    def insert_tail(self, e):
        """
        Add a node in the tail of a list.
        :param e:
        :return:
        """
        newest = Node(e, None)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.pointer = newest
        self.tail = newest
        self.size += 1
        return newest

    def delete_head(self):
        if self.head is None:
            print('The list is empty.')
        else:
            element = self.head.element
            self.head = self.head.pointer
            self.size -= 1
            return element

    def iterate(self):
        pointer = self.head
        print('The element in the list: ')
        while pointer is not None:
            print(pointer.element)
            pointer = pointer.pointer

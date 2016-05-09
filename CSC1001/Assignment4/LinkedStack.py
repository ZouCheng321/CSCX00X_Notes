class Node:
    def __init__(self,element,pointer):
        self.element = element
        self.pointer = pointer
        
class LinkedStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self,e):
        self.head = Node(e,self.head)
        self.size += 1

    def top(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            return self.head.element

    def pop(self):
        if self.is_empty():
            print('Stack is empty.')
        else:
            answer = self.head.element
            self.head = self.head.pointer
            self.size -= 1
            return answer


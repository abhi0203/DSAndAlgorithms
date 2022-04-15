# This file implements the stack using linked list. 


class Node:
    def __init__(self, value):
        self.value= value
        self.next= None


class LinkedList:
    def __init__(self):
        self.head= None
        self.tail= None

    def __iter__(self):
        currentNode= self.head
        while currentNode:
            yield currentNode
            currentNode= currentNode.next


class stack:
    def __init__(self):
        self.stack= LinkedList()
    
    def isEmpty(self):
        if self.stack.head== None:
            return True
        else:
            return False
    
    def __str__(self):
        value= [str(x.value) for x in self.stack]
        #print(value)
        return '\n'.join(value)

    def push(self, value):
        stackNode= Node(value)
        if self.stack.head is None:
            self.stack.head= stackNode
            self.stack.tail= stackNode
        else:
            stackNode.next= self.stack.head
            self.stack.head= stackNode
    

    def pop(self):
        if self.stack.head is None:
            print("Stack is empty nothing to pop")
            return None
        else:
            value= self.stack.head.value
            self.stack.head= self.stack.head.next
            return value
    
    def peek(self):
        if self.stack.head is None:
            print("Stack is empty")
            return None
        else:
            return self.stack.head.value


newStack= stack()
newStack.push(1)
newStack.push(2)
newStack.push(3)

print(newStack)
newStack.pop()
print("After popping")
print(newStack)
print("After peeiking")
print(newStack.peek())


    
# Queue Class


class Node:
    def __init__(self, value):
        self.value= value
        self.next= None

    def __str__(self):
        nodeValue= [str(x) for x in self.value ]


class LinkedList:
    def __init__(self):
        self.head= None
        self.tail= None

    def __iter__(self):
        currentNode= self.head
        while currentNode:
            yield currentNode
            currentNode= currentNode.next
    
class Queue:
    def __init__(self):
        self.queue= LinkedList()
    

    def __str__(self):
        value= [str(x.value) for x in self.queue]
        return " ".join(value)

    
    def isEmpty(self):
        if self.queue.head is None:
            return True
        else:
            return False
        
    
    def enqueue(self, value):
        node= Node(value)
        if self.isEmpty():
            self.queue.head= node
            self.queue.tail= node
        else:
            self.queue.tail.next= node
            self.queue.tail= node
    
    def dequeu(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        else:
            value= self.queue.head.value
            headNode= self.queue.head
            if self.queue.head== self.queue.tail:
                self.queue.head= None
                self.queue.tail= None
                return value
            else:
                self.queue.head= headNode.next
                headNode.next= None
                return value

    def peek(self):
        if not self.isEmpty():
            return self.queue.head.value
        else:
            print("Empty Qyeye")
            return None
    

queue= Queue()
print("Empty queue")
print(queue)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print("Full Queue")
print(queue)

print(queue.dequeu())
print("After dequeu")
print(queue)

print("Peek")

print(queue.peek())


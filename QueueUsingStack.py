'''
Creating a queue using a a stack.
Use 2 stacks.

As long as we are enquing, we push to the first stack.

Then when we call dequeue, we first check second stack.
    If second stack is empty, then we pop everything from frist stack
and then pop the topmost item.

If the second stack is not empty, we just pop from second stack stack.

'''

class stack:
    def __init__(self):
        self.stack=[]
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack)==0:
            print("Stack is empty")
        else:
            return self.stack.pop()

    def __len__(self):
        return len(self.stack)


class QueueWithStacks:

    def __init__(self):
        self.inStack= stack()
        self.outStack= stack()

    def enqueue(self, item):
        self.inStack.push(item)

    def dequeue(self):
        if len(self.outStack)>0:
            return self.outStack.pop()
        else:
            while len(self.inStack):
                self.outStack.push(self.inStack.pop())
            return self.outStack.pop()


q= QueueWithStacks()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())


q.enqueue(6)
q.enqueue(7)


print(q.dequeue())
print(q.dequeue())
print(q.dequeue())



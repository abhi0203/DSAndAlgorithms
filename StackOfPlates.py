'''
Create a stack of plates. 
At any time, the stack can have some max number of plates.
If the plates crosses that number, then automatically another stack is created.
When it comes for popping, we are popping from the most recent plate stack first.
We can also give specific number of stack from where user can ask us to pop.

Logic:
- This of this as list of stacks. 
- As the capacity of stack at one index comes to an end, we append another item to the stack and so on.
- When it comes to popping, we can pop from the last item in the stack. 

init():
- Just define the maxsize of the stack

push()
- Check if therre are more than one items in the list. 
    - More than one item indicates that 2D array has been formed.
- If there are more than one item in the list, then check the length of the last item is less than maxsize.
    - if both the conditions are satisfied, then add an item at the top of last element.
- Else:
    - Append the item in the master stack as an list.    


isEmpty()
- Check if the stack is empty

pop()
- Check if the stack is empty. If yes return 0 
- Else return last items in stack .pop()

popAt()
- Check if the value is > 0 and <= maxlen
- Check if there are items in the choice of stack
- If uye pop the last ite.m


'''

class StackOfPlates():
    def __init__(self, maxSize):
        self.maxSize= maxSize
        self.stack= []

    def __str__(self):
        return self.stack
    
    def push(self, item):
        if len(self.stack)> 0 and len(self.stack[-1])< self.maxSize:
            self.stack[-1].append(item)
        else:
            self.stack.append([item])

    def isEmpty(self):
        if self.stack==[]:
            return True
        return False
    
    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        # Keep popping from master stack till you reach a child stack which has some value
        while len(self.stack) and len(self.stack[-1])==0:
            self.stack.pop()
        if len(self.stack)>0:
            return self.stack[-1].pop()

    def popAt(self, stackNum):
        masterStackLen= len(self.stack)
        if stackNum<=0 or stackNum> masterStackLen:
            return "Incorrect Stack number"
        while len(self.stack) and len(self.stack[stackNum-1])==0:
            self.stack.pop(stackNum-1)
            if stackNum > len(self.stack):
                break
        if len(self.stack)>= stackNum:
            return self.stack[stackNum-1].pop()
        else:
            return "No stack at given place. "




stackOFStack= StackOfPlates(3)

stackOFStack.push(1)
stackOFStack.push(2)
stackOFStack.push(3)
stackOFStack.push(4)
stackOFStack.push(5)
stackOFStack.push(6)

print(stackOFStack.pop())
print(stackOFStack.popAt(2))
print(stackOFStack.popAt(2))
print(stackOFStack.popAt(2))
print(stackOFStack.popAt(1))



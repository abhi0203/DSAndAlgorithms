'''
Need to create 3 stacks using a single list
- Implment basic stack methods isEmpty and isFull, push, pop and peek
- length of each stack should be given.
- While using push, pop and peek methods, input will be given in terms of whihc stack to push to.

Approach:

Init
- Get the size of the single stack from user
- Based on this value, create a 3x bigger list and add 0 to it.
- Also create a value for top for all the stacks.
- We also need to maintain the max length so that we dont overflow the length.

isFull
- Get the input interms of which stack the user wants to check.
- Based on the input, create an offset i.e. multiply it stacksize. This will give us an base offset.
- Check the value of top for that offset and if it is equal to Max Len -1. If yes, return True
- Else Return False.

isEmpty
- Check the value of the top variable for the correxponding stack. 
- if it is 0, then the stack is empty.


push()
- Get the number of stack on which you want to push.
- Check if that stack is full. 
- If the stack has space, increment the value of that top by 1
- Calculate the offset in actual list by newTop= (stacknumber * 10) + currentTop + 1 
- Use the above new top to push the values.
- return if the number is pushed or not.

peek()
- Check if the stack is empty
- Get the stack number and return the value at the top of that stack number.

'''

class ThreeStack:
    def __init__(self, stackSize):
        self.numberOfStacks= 3
        self.stack= [0] * (self.numberOfStacks*stackSize)
        self.top= [-1]* (self.numberOfStacks)
        self.stackMaxLen= stackSize

    def isFull(self, stackNum):
        if stackNum< 1 or stackNum>3:
            return "Invalid Stack Number"  
        if self.top[stackNum-1]< self.stackMaxLen-1:
            return False
        else:
            if self.top[stackNum]==self.stackMaxLen-1:
                return True

    def isEmpty(self, stackNum):
        if stackNum<1 or stackNum>3:
            return "Invalid Stack Number"
        elif self.top[stackNum-1]==-1:
            return True
        else:
            return False

    def push(self, stackNum, value):
        if stackNum<1 or stackNum>3:
            return "Invalid Stack Number"
        if self.isFull(stackNum):
            return "Stack is Full"
        else:
            newTopOffset= (stackNum * self.stackMaxLen) + self.top[stackNum]+1
            self.stack[newTopOffset]= value
            self.top[stackNum]+=1
            return "The number is pushed"

    def peek(self, stackNum):
        if stackNum<1 or stackNum>3:
            return "Invalid stack number"
        else:
            if self.isEmpty(stackNum):
                return "Stack is empty"
            else:
                return self.stack[self.top[stackNum]]

    

    
threeStack= ThreeStack(5)
print(threeStack.isFull(1))
print(threeStack.isEmpty(3))        

print(threeStack.push(1,5))
print(threeStack.peek(1))   
        





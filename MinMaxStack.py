# Feel free to add new properties and methods to the class.

class Node:
	def __init__(self, minVal, maxVal, value= None):
		self.value= value
		self.minVal= minVal
		self.maxVal= maxVal
		self.next= None
		
class LinkedList:
	def __init__(self):
		self.head= None

class MinMaxStack:
    def __init__(self):
        self.stack= LinkedList()
    
    def peek(self):
        if self.stack.head is not None:
            return self.stack.head.value

    def pop(self):
        # Write your code here.
        if self.stack.head is None:
            return None
        else:
            poppedValue= self.stack.head
            self.stack.head= poppedValue.next
            poppedValue.next= None
            return poppedValue.value

    def push(self, number):
        # Write your code here.
        newNode= Node(number,number, number)
		
        if self.stack.head is None:
            self.stack.head= newNode
            return
		
        newNode.next= self.stack.head
		
        if number<= self.stack.head.minVal:
            newNode.minVal= number
            newNode.maxVal= self.stack.head.maxVal	
        elif number >= self.stack.head.maxVal:
            newNode.maxVal= number
            newNode.minVal= self.stack.head.minVal
        else:
            newNode.minVal= self.stack.head.minVal
            newNode.maxVal= self.stack.head.maxVal
		
        self.stack.head= newNode
		

    def getMin(self):
        # Write your code here.
        if self.stack.head is not None:
            return self.stack.head.minVal

    def getMax(self):
        # Write your code here.
        if self.stack.head is not None:
            return self.stack.head.maxVal


st= MinMaxStack()

st.push(2)
print("Pass 1")
print(st.peek())
print(st.getMin())
print(st.getMax())
st.push(7)
print("Pass 2")
print(st.peek())
print(st.getMin())
print(st.getMax())
st.push(1)
print("Pass 3")
print(st.peek())
print(st.getMin())
print(st.getMax())
st.push(8)
print("Pass 4")
print(st.peek())
print(st.getMin())
print(st.getMax())
st.push(3)
print("Pass 5")
print(st.peek())
print(st.getMin())
print(st.getMax())
st.push(9)
print("Pass 6")
print(st.peek())
print(st.getMin())
print(st.getMax())
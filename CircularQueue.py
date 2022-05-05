# Code to create a circular queue with a list data structure

'''
init
- Create a queue with maxsize variable. So we limit the size of the list.
- While initializing, create the list that as the maxsize variable and assign it to None. 
- Also assign the front and rear to -1

isEmpty
- If the rear is equivalent to -1, the the queue must be empty.

isFull
- There are multiple cases here.
    - If we are not in circular feature, 
        - rear has to be equal to maxlength of the queue while front has to be on 0
    - If we are in circulr feature, then rear+1 should point to first. 
- If none of the above cases match, the queue is not Full

enqueue:
- One case is Queue is empty
- One case is Queue is full
    - In this case we cant enqueue so return some message
- One case is simple entry
- One case is circular entry

dequeue:
- Queue is empty
- Queue is full
- There is only one element in the queue
- front is pointing to the last element and we have to go round the circle


'''


class CircularQueue:
    def __init__(self, maxsize):
        self.queue= maxsize * [None]
        self.maxsize= maxsize
        self.front= -1 
        self.rear= -1


    def __str__(self):
        queueList= [str(x) for x in self.queue]
        return "<-".join(queueList)

    def isEmpty(self):
        return self.rear==-1

    def isFull(self):
        if self.isEmpty():
            return False
        if self.front== 0 and self.rear+ 1== self.maxsize:
            return True
        elif self.rear+ 1== self.front:
            return True
        else:
            return False
    
    def enqueue(self, value):
        if self.isFull():
            return "The queue is full"
        if self.rear==-1:
            self.front+=1
            self.rear+=1
            self.queue[self.front]= value
        elif self.rear+1== self.maxsize:
            self.rear= 0
            self.queue[self.rear]= value
        else:
            self.rear+=1
            self.queue[self.rear]=value
        
        return "The element is added into queue"

    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        if self.front== self.rear:
            current= self.queue[self.front]
            self.queue[self.front]= None
            self.front= -1
            self.rear= -1
        elif self.front+1== self.maxsize:
            current= self.queue[self.front]
            self.queue[self.front]= None
            self.front= 0 
        else:
            current= self.queue[self.front]
            self.queue[self.front]= None
            self.front+=1
        
        return current




circQueue=  CircularQueue(4)

print(circQueue.isEmpty())
print(circQueue.isFull())

circQueue.enqueue(1)
circQueue.enqueue(2)
circQueue.enqueue(3)
circQueue.enqueue(4)

print(circQueue.isEmpty())
print(circQueue.isFull())
print(circQueue)

print(circQueue.dequeue())
print(circQueue)
print(circQueue.dequeue())
print(circQueue)
print(circQueue.dequeue())
print(circQueue)
print(circQueue.dequeue())
print(circQueue)
print(circQueue.isEmpty())
print(circQueue.isFull())





    

    

    



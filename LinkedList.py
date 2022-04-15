# Generic Linked List class that can be used for all other problems.

# creating a node class
# Here I am creating both the prev and next variable, but prev need not be used making it a singly linked list.

from random import randint

class Node:
    def __init__(self, value= None):
        self.value= value
        self.next= None
        self.prev= None
    
    # Override the str method provided in python to return the value of the node
    def __str__(self):
        return str(self.value)


# Create a class Linked List that has following methods
# init, iter, str, len, add (always add node to end), generage (generate a random list for a range)

class LinkedList:
    def __init__(self):
        self.head= None
        self.tail= None
    
    def __iter__(self):
        node= self.head
        while node:
            yield node
            node= node.next

    # Below method will iterate through the nodes of list one by one and convert the values into a string.
    # It will then use list join method to append -> to give us an impression of the list.
    def __str__(self):
        values= [str(x.value) for x in self]
        return "->".join(values)

    
    def __len__(self):
        # List can be empty in which case return 0 or else return the length
        if self.head is None:
            print("List is empty")
            return 0
        else:
            node= self.head
            listLen= 0
            while node:
                listLen+=1
                node= node.next
            return listLen
    
    def add(self, value):
        # Assume that for now always add at the end of the list
        # if the list is empty then add it as first value. else append it at the end
        newNode= Node(value)
        if self.head is None:
            self.head= newNode
            self.tail= newNode
        else:
            self.tail.next= newNode
            self.tail= newNode
    
    def generate(self, n, min_value, max_value):
        # This method generates the a list based on value n which represent how many items should be there in the list.
        # The node value will be between min_value and max_value

        # Just to be on the safer side, start fresh and assign head and tail to None
        self.head= None
        self.tail= None

        # Iterate thrrough n and call add() method to keep adding the nodes
        # use min and max int value in the add method
        for i in range(n):
            self.add(randint(min_value, max_value))
        
        # return the list object at the end
        return self


#llA= LinkedList()
#llA.generate(10, 0, 99)
#print(llA)
#print(len(llA))





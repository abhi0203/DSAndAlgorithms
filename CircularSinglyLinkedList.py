# Following is the code for Circular Sinlgy Linked List.
# It is supposed to have following functionalities out of the box.
# 1. Create a Circular Linked List
# 2. Insert into a CLL
# 3. Traverse the CLL
# 4. Display CLL as List
# 5. Traverse and find an item in the list
# 6. Display list items
# 7. Delete an item from the list
# 8. Delete entire CLL

# Create a node class
class Node:
    def __init__(self, value= None):
        self.value= value
        self.next = None

# Create a class Circular Linked List that has implementation of all above methofds

class CircularLinkedList:
    def __init__(self):
        self.head= None
        self.tail= None
    
    # Following method creates an iteration fucntion that displays the list as the list.

    def __iter__(self):
        node= self.head
        while node:
            yield node
            node= node.next
            if node== self.head:
                break
    
    # Method to Insert into a Circular Linked List
    # 1. Insert at head
    #   - List can be empty
    #   - List can already have some items
    # 2. Insert at tail
    #   - List can be empty
    #   - List already have some items
    # 3. Insert at some location
    #   - List has some items and valid location
    #   - List is empty and locations is first or end location
    #   - List is non empty and location is first or last location
    #   - List is non empty and location is out of bounds
    
    def insertCSLL(self, value, location):
        node = Node(value)
        if location== 1:
            if self.head is None:
                self.head= node
                self.tail= node
                node.next= node
            else:
                headNode= self.head
                tailNode= self.tail
                self.head= node
                node.next = headNode
                tailNode.next= node
        elif location== -1:
            if self.head== None:
                self.head= node
                self.tail= node
                node.next= node
            else:
                headNode= self.head
                tailNode= self.tail
                node.next= headNode
                tailNode.next= node
                self.tail= node
        else:
            index= 1
            currentNode= self.head
            while index< location -1 and currentNode.next is not self.head:
                currentNode= currentNode.next
                index+=1
            #1-> 2-> 3-> 4-> 1   5=4
            # - location is by chance last lcation
            # - location is somewhat in the middle
            # - location is absurd and much greater than length
            if currentNode.next== self.head:
                # Case to handle if location is by chance last
                if index+1 == location:
                    node.next= self.head
                    currentNode.next= node
                    self.tail= node
                else: # Case to handle some absurd location
                    print("location > len(CLL). hence returning None")
                    return None
            else: # Case to handle a node in the middle
                node.next= currentNode.next
                currentNode.next= node
    
    # Method to traverse the CSLL and display items one by one
    def traverseCSLL(self):
        # Check if the list is empty
        if self.head is None:
            print("The list is empty and nothing to display. Returning None")
            return None
        # Start with head node, display the value move to next node
        # If the next node is head node break
        currentNode= self.head
        while currentNode:
            print(currentNode.value)
            if currentNode.next== self.head:
                break
            currentNode= currentNode.next
        # 1-> 2-> 3-> head    

    # Method to check if a particular value is present in the CSLL
    def searchCSLL(self, value):
        # Check if the list is empty. 
        if self.head is None:
            print("List is empty. Nothing to search. Returning False")
            return False
        # Start with head node. Compare the value. If matches return true. Else move to next node
        # Traverse all the way till the last node and then break the loop with value not found
        currentNode= self.head
        while currentNode:
            if currentNode.value== value:
                print("Item is present and it is "+ str(value))
                return True
            else:
                currentNode= currentNode.next
                if currentNode== self.head:
                    break
        print("Value is not present.")
        return False
        

    # Method to delete an item from the CSLL
    # Following are the cases
    # 1. Deleting first item
    #   - If the list is empty
    #   - the list is not empty
    #   - List has only one item
    # 2. Deleting last item
    #   - List is empty
    #   - List is not empty
    #   - List has only one item
    # 3. Deleting the item at a location
    #   - List is empty
    #   - List is not empty and item in middle
    #   - List is not empty and item by chance is last
    #   - List is not empty and location> len(list)
    def deleteItemCSLL(self, location):
        # Check for the empty condition 
        if self.head is None:
            print("CSLL is empty and nothing to delete. returning None")
            return None
        
        # Check for first item deleting
        if location== 1:
            # Check if there is only one item in the list
            if self.head== self.tail:
                self.head= None
                self.tail.next= None
                self.tail= None
            else:
                headNode= self.head
                self.head= headNode.next
                self.tail.next= self.head
                headNode.next= None
        elif location== -1: 
            # Check if there is only one node in the CSLL
            if self.head== self.tail:
                self.head= None
                self.tail.next= None
                self.tail= None
            else:
                # traverse till last but one node
                # move the pointer to right location
                currentNode= self.head
                while currentNode.next is not self.tail:
                    currentNode= currentNode.next
                # We are not at last but one node
                currentNode.next= self.head
                self.tail.next= None
                self.tail= currentNode
        else:
            index= 1
            currentNode= self.head
            # Move till the location we want to delete
            # Check if this is a middle node, if it is, delete the nodes
            # If by chance it is last node, delete pointers accordingly
            # If the location is out of boundes, print the message accordingly.
            while index< location-1 and currentNode.next is not self.head:
                currentNode= currentNode.next
                index+= 1
            
            # Check on what condition the while loop ended
            # If it ended as list ended on tail
            #   - then check if the locaiton is by chance last location else it is invalid location
            # 1-> 2-> 3-> 4-> head  5=3
            if currentNode.next is self.head:
                print("trying to delete an invalid node. returning None")
                return None
            else:
                # Check if this is last Node
                if currentNode.next== self.tail:
                    currentNode.next= self.head
                    self.tail.next= None
                    self.tail= currentNode
                else: # The node is something in between
                    currentNode.next= currentNode.next.next
                    currentNode.next.next= None
            print("Node is deleted")





    # Method to delete entire CSLL
    def deleteCSLL(self):
        # If the CSLL is empty there is nothing to delete
        if self.head is None:
            print("List empty and nothing to delete. retruning none")
            return None
        self.head= None
        self.tail.next= None
        self.tail= None

    


circularSLL = CircularLinkedList()
circularSLL.insertCSLL(1,1)
circularSLL.insertCSLL(2,2)
circularSLL.insertCSLL(3,3)
circularSLL.insertCSLL(4,-1)
circularSLL.insertCSLL(5,5)
circularSLL.insertCSLL(6,3)

print([node.value for node in circularSLL]) 

circularSLL.deleteItemCSLL(5)

print([node.value for node in circularSLL]) 

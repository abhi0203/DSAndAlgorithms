# Code to create basic methods of doubly linked list.

# Following are the methods that we need to implement
# 1. Create a DLL
# 2. Insert an item into DLL at various positions
# 3. Traverse a DLL
# 4. Reverse Traverse a DLL
# 5. Search an item into DLL
# 6. Delete an item from a position in DLL
# 7. Delete entire DLL

# Create a class node. This node will have prev as well as next pointer.

from CircularSinglyLinkedList import CircularLinkedList


class Node:
    def __init__(self, value= None):
        self.value= value
        self.next= None
        self.prev= None

# Cerate a class doubly Linked list. This will have all the necessary methods.

class DoublyLinkedList:
    def __init__(self):
        self.head= None
        self.tail= None
    
    # Define the iter function to print the DLL as simple list

    def __iter__(self):
        node= self.head
        while node:
            yield node
            node= node.next
            if node is self.head:
                break

    # 
    # Define a method to insert an item into the list
    # following are the cases that are considered here.
    # 1. Insert at the head
    #   - If the list is emoty
    #   - If the list has items
    # 2. Insert at the tail
    #   - If the list is emoty
    #   - If the list has items 
    # 3. Insert somewhere in between using location parameter
    #   - If the location parameter == last
    #   - If the location parameter is first
    #   - If location is in between
    #   - If the location > len(DLL)
    
    def insertDLL(self, value, location):
        # Create a new node and assign its prev and next to none
        newNode= Node(value)
        # Case fo inserting at head
        if location== 1:
            if self.head is None:
                self.head= newNode
                self.tail= newNode
            else:
                newNode.next= self.head
                self.head.prev= newNode
                self.head= newNode
        elif location== -1:
            if self.head is None:
                self.head= newNode
                self.tail= newNode
            else:
                self.tail.next= newNode
                newNode.prev= self.tail
                self.tail= newNode
        else:
            index= 1
            currentNode= self.head
            # 1-> 2-> 3->4-> None 5=4
            while index< location-1 and currentNode is not self.tail:
                currentNode= currentNode.next
                index+=1 
            
            if currentNode is self.tail:
                if index+1 == location:
                    #This location represent allocating at the end
                    newNode.prev= self.tail
                    self.tail.next= newNode
                    self.tail= newNode
                else:
                    print("locaiton > len(DLL). Please give correct location. Return None")
                    return None
            else:
                newNode.next= currentNode.next
                newNode.prev= currentNode
                currentNode.next.prev= newNode
                currentNode.next= newNode

    # Define the method to traverse the DLL from head to tail
    def traverse(self):
        if self.head is None:
            print("List is enpty")
            return
        currentNode= self.head
        while currentNode:
            print(currentNode.value)
            currentNode= currentNode.next

    # Define a method to trverse from tail to head
    def revTraverse(self):
        if self.tail is None:
            print("List is empty")
            return None
        currentNode= self.tail
        while currentNode:
            print(currentNode.value)
            currentNode= currentNode.prev
        
    def searchItem(self, value):
        if self.head is None:
            print("List is empty. returning none")
            return None
        currentNode= self.head
        while currentNode:
            if currentNode.value== value:
                print("Value found "+ str(value))
                return
            currentNode= currentNode.next
        print("Value is not found")
    

    # Define a method to delete an item
    # 1. Delete the head value
    #   - list is empty
    #   - list has only one item
    #   - list has multiple items
    # 2. Delete the tail value
    #   - list is empty
    #   - list has only one value
    #   - list has multiple values
    # 3. Delete the item based one some location
    #   - list is empty
    #   - location > len(list)
    #   - location is somewhere in the middle
    #   - location is by chance the end

    def deleteItem(self, location):
        if self.head== None:
            print("List is empty.")
            return
        else:
            if location== 1:
                if self.head== self.tail:
                    self.head= None
                    self.tail= None
                else:
                    headNode= self.head
                    headNode.next.prev= None
                    self.head= headNode.next
                    headNode.next= None
            elif location== -1:
                if self.head== self.tail:
                    self.head= None
                    self.tail= None
                else:
                    currentNode= self.head
                    while currentNode is not self.tail:
                        currentNode= currentNode.next
                    self.tail= currentNode.prev
                    currentNode.prev= None
                    self.tail.next= None
            else:
                currentNode= self.head
                index= 1
                # 1-> 2-> 3-> 4-> 5-> None  6=5
                while index< location-1 and currentNode.next is not None:
                    currentNode= currentNode.next 
                    index+=1 
                
                if currentNode.next is None:
                    print("Invalid location of delete. Return None")
                    return None
                elif currentNode.next is self.tail:
                    # By chance the node to be deleted is last node
                    currentNode.next = None
                    self.tail.prev= None
                    self.tail= currentNode
                else:
                    deleteNode= currentNode.next
                    nextNode= deleteNode.next
                    currentNode.next= nextNode
                    nextNode.prev= currentNode
                    deleteNode.next= None
                    deleteNode.prev= None

                

doublyLL= DoublyLinkedList()
doublyLL.insertDLL(1,1)
doublyLL.insertDLL(2,2)
doublyLL.insertDLL(3,3)
doublyLL.insertDLL(4,-1)
doublyLL.insertDLL(5,5)

print("List after insert")
print([node.value for node in doublyLL])

#print("List Traversal")
##doublyLL.traverse()
#print("List reverse traversal")
#doublyLL.revTraverse()
#print("Trying to find a value")
#doublyLL.searchItem(4)

print("Trying to delete")
doublyLL.deleteItem(4)
print([node.value for node in doublyLL])

            



        

     


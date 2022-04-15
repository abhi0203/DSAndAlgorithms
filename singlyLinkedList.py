# Following methods are supported
# 1. Create a list with head and tail
# 2. Insert into the list 
#    - At the beginning
#    - In the middle
#    - At the end
# 3. Traverse through the list
# 4. Delete from the list
#    - At the beginning
#    - In the middle
#    - At the end
# 5. Search the value in the list
# 6. Delete the entire list
# 7.     

# Create class node that represents the node linked list

class Node:
    def __init__(self, value= None):
        self.value= value
        self.next= None

# Create a class Linked List that creates the list and assign head and tail element to None

class SinglyLinkedList:
    # Initialize the List
    def __init__(self):
        self.head= None
        self.tail= None
    
    # Create and iterator using yeild funciton
    # This should just print the list
    def __iter__(self):
        node= self.head
        while node:
            yield node
            node= node.next

    
    # Insert into the list based on positions. 
    # 0 means at the head, -1 means at the tail and some other positive number means at that locations

    def insertSLL(self, value, location):
        newNode= Node(value)

        # Code to insert at head
        if location==1:
            if self.head is None:
                #print("inside if for location 0")
                self.head= newNode
                self.tail= newNode
            else:
                newNode.next= self.head
                self.head= newNode
        elif location==-1: # Code to insert the node at the end
            #print("inside if for location 1")
            if self.head is None:
                self.head= newNode
                self.tail= newNode
            else:
                currentNode= self.head
                while currentNode.next is not None:
                    currentNode= currentNode.next
                currentNode.next= newNode
                self.tail= currentNode.next
        else:# Code to insert a node at the middle
            if self.head is None:
                print("List is empty and cant insert in the middle")
                return None
            else:
                #print("inside else for some location ")
                index= 1
                currentNode= self.head
                while index < location-1 and currentNode:
                    currentNode= currentNode.next
                    index+=1
                # 1-> 2-> 3-> 4-> 5-> None
                # Code to handle in case location > len(singlyLinkedList)
                if currentNode is None:
                    print("You are trying to insert at wrong position. returning None")
                    return None
                newNode.next= currentNode.next
                currentNode.next= newNode
    
    # Code to print the list
    def viewList(self):
        print("Inside View List")
        if self.head is None:
            print("List is empty nothing to print. Returning None")
            return None
        else:
            currentNode= self.head
            while currentNode is not None:
                print(currentNode.value)
                currentNode= currentNode.next

    # Code to search a value in the list
    # This will return first occurance of that value

    def findItem(self, value):
        if self.head is None:
            print("List is empty")
            return None
        currentNode= self.head
        while currentNode:
            if currentNode.value== value:
                print("Found what you are looking for")
                return currentNode.value
            currentNode= currentNode.next
        
        print("Value not present in the list")
        return None

    # Code to delete entire list
    def deleteEntireList(self):
        if self.head is None:
            print("List already empty")
            return None
        self.head= None
        self.tail= None

    
    # Code to delete a node from the linked list
    
    def deleteItem(self, location):
        # 1. Check if the list is empty
        if self.head is None:
            print("List is empty. cant delete. returning None")
            return None
        
        if location==1:#If list is not empty and you want to delete the item at head.
            # if there is only one node
            if self.head== self.tail:
                self.head = None
                self.tail = None
            else:
                currentNode= self.head
                self.head= currentNode.next
                currentNode.next= None
        elif location==-1: # If the list is not empty and someone wants to delete tail location
            if self.head== self.tail: # There is only one node and someone deletes tail
                self.head = None
                self.tail = None
            else:
                #Traverse till last but one node and then make adjustments
                currentNode= self.head
                while currentNode.next.next is not None:
                    currentNode= currentNode.next
                self.tail = currentNode
                currentNode.next= None
        else: # Want to delete somewhere in the middle
            index =1
            currentNode= self.head
            #1-> 2-> 3-> 4-> 5-> None
            while index < location-1 and currentNode is not None:
                currentNode= currentNode.next
                index+=1
            # Check if location > len(linkedLL)
            if currentNode is None:
                print("Incorrect location of delete is given. Returning None")
                return None
            delNode= currentNode.next
            currentNode.next= delNode.next
            print("Deleting the node "+ str(currentNode.next.value))
            delNode.next= None

        


#Test Code
linkedList= SinglyLinkedList()
#linkedList.viewList()

linkedList.insertSLL(1,1)
linkedList.insertSLL(2,2)
linkedList.insertSLL(3,-1)
linkedList.insertSLL(4,-1)
linkedList.insertSLL(5,-1)
#linkedList.viewList()
print("Initial Linked List")
print([node.value for node in linkedList]) 

linkedList.insertSLL(6,6)
print("Linked List after insert")
print([node.value for node in linkedList]) 

print("Linked List after find")
print(linkedList.findItem(5))

linkedList.deleteItem(3)
print("Linked List after delete")
print([node.value for node in linkedList]) 


print("After deleting entire linked list")
linkedList.deleteEntireList()
print([node.value for node in linkedList]) 
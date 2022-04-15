# Code to create basic methods of circular doubly linked list.

# Following are the methods that we need to implement
# 1. Create a DLL
# 2. Insert an item into DLL at various positions
# 3. Traverse a DLL
# 4. Reverse Traverse a DLL
# 5. Search an item into DLL
# 6. Delete an item from a position in DLL
# 7. Delete entire DLL


# Create a node class with prev and next pointer

class Node:
    def __init__(self, value= None):
        self.value= value
        self.prev= None
        self.next= None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head= None
        self.tail= None 

    def __iter__(self):
        node= self.head
        while node:
            yield node
            node= node.next
            if node is self.tail.next:
                break
    
    # Create the Linked List
    # Following cases are covered.
    # 1. Adding the new node at the head
    #   - There are no nodes in the list
    #   - There are some nodes in the list
    # 2. Adding new node at the tail
    #   - There are no nodes in the list
    #   - There are some nodes in the list
    # 3. Adding a new node somewhere in the middle
    #   - There are no nodes present in the list
    #   - There are some nodes present in the list
    #       - The node to be inserted is in the middle
    #       - The node locaiton is by chance last

    def insertCDLL(self, value, location):
        newNode= Node(value)
        if location==1:
            if self.head is None:
                newNode.prev= newNode
                newNode.next= newNode
                self.head= newNode
                self.tail= newNode
            else:
                newNode.next= self.head
                newNode.prev= self.tail
                self.tail.next= newNode
                self.head.prev= newNode
                self.head= newNode
        elif location== -1:
            if self.head is None:
                newNode.next= newNode
                newNode.prev= newNode
                self.head= newNode
                self.tail= newNode
            else:
                newNode.prev= self.tail
                newNode.next= self.head
                self.tail.next= newNode
                self.head.prev= newNode
                self.tail= newNode
        else:
            currentNode= self.head
            index= 1
            # 1-> 2-> 3-> First 
            while index< location-1 and currentNode.next is not self.head:
                currentNode= currentNode.next
                index+=1

            if currentNode is self.tail:
                if index+1== location:
                    # Adding the node to the last
                    newNode.next= self.head
                    newNode.prev= self.tail
                    self.tail.next= newNode
                    self.head.prev= newNode
                    self.tail= newNode
                else:
                    print("Some invalid location is given")
                    return None
            else:
                # node needs to be moved from somewhere in the middle
                nextNode= currentNode.next
                newNode.next= nextNode
                newNode.prev= currentNode
                currentNode.next= newNode
                nextNode.prev= newNode

    # Code to traverse the list

    def traverse(self):
        if self.head is None:
            print("List is emoty")
            return None
        node= self.head
        while node:
            print(node.value)
            node= node.next
            if node is self.head:
                break
    
    # Code to reverse traverse a list

    def reverseTraverse(self):
        if self.head is None:
            print("List is empty")
            return None
        node= self.tail
        while node:
            print(node.value)
            node= node.prev
            if node is self.tail:
                break
    
    # Code to search an item in the list

    def searchItem(self, value):
        if self.head is None:
            print("List is emoty")
            return None
        node= self.head
        while node:
            if node.value== value:
                print("Value Found")
                return
            node= node.next
            if node is self.head:
                print("Value is not present")
                break
    
    # Code to delete an item from the list

    def deleteItem(self, location):
        if self.head is None:
            print("List empty")
            return
        if location== 1:
            currentNode= self.head
            if self.head == self.tail:
                # List has only one item
                currentNode.prev= None
                currentNode.next= None
                self.head= None
                self.tail= None
            else:
                # List has multiple Nodes
                currentNode.next.prev= self.tail
                self.tail.next= currentNode.next
                self.head= currentNode.next
                currentNode.next= None
                currentNode.prev= None
        elif location== -1:
            currentNode= self.tail
            if self.head== self.tail:
                # List has only one item
                currentNode.prev= None
                currentNode.next= None
                self.head= None
                self.tail= None
            else:
                currentNode.prev.next= self.head
                self.head.prev= currentNode.prev
                self.tail= currentNode.prev
                currentNode.next= None
                currentNode.prev= None
        else:
            index= 1
            currentNode= self.head
            while index< location-1 and currentNode.next is not self.head:
                currentNode= currentNode.next
                index+=1
            # 1-> 2-> 3-> head

            if currentNode.next is self.head:
                print("Incorrect value given for deletion")
                return None
            else:
                if currentNode.next is self.tail:
                    # Need to delete last node
                    currentNode.next= self.head
                    self.head.prev= currentNode
                    self.tail.next= None
                    self.tail.prev= None
                    self.tail= currentNode
                else:
                    # Need to delete middle node
                    currentNode.next.next.prev= currentNode
                    currentNode.next= currentNode.next.next
            return



circularDLL = CircularDoublyLinkedList()
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,2)
circularDLL.insertCDLL(3,3)
circularDLL.insertCDLL(4,2)
print([node.value for node in circularDLL])

print("After traverse")
circularDLL.traverse()
print([node.value for node in circularDLL])


print("After  reverse traverse")
circularDLL.reverseTraverse()
print([node.value for node in circularDLL])


print("After delete")
circularDLL.deleteItem(2)
print([node.value for node in circularDLL])

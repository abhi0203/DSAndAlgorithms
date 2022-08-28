# Create by Abhiram
# This file has binary tree implemented using Linked List Method.
# I am also implementing different methtods related to the Binary tree.
# Pre-Order, In-Order and Post Order traversal. I am also implementing the level order traversal which is similar to Breadth first search for the graphs.
# Searching an element. Adding an element and deleting an element and its different conditions.

from logging import root
from queue import Queue as q

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild= None
        self.rightChild= None


rootNode= TreeNode("Drinks")
rootNode.leftChild= TreeNode("Cold")
rootNode.rightChild= TreeNode("Hot")


# Pre order traversal is Center-> Left -> Right
# Time complexity is O(N) as we have to traverse through each and every node. 
# Space Complexity is O(n) since we are using the recursive way, we have to use the stack in ram.
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

print("Pre Order Traversal")
preOrderTraversal(rootNode)

# Inorder Traversal is Left -> Center -> Right
# Time complexity is again O(n) as we have to traverse through n items
# Space complexity is also O(n) as we are using the stacks in the recursive calls.
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

print("In Order Traversal")
inOrderTraversal(rootNode)

# Post order traversal is Left -> Right-> center
# This to is O(n) from both time and space complexity.
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

print("Post Order Traversal")
postOrderTraversal(rootNode)

# This is the code for Level order traversal.
# This is also the BFS way of accessing the binary tree.
# Here we add the elements to the queue as we traverse them and then dequeue them one by one in order to access their child elements.
# Time complexity is O(n) as we have to go through all the elements. Space is also O(n) as I think we have to add all the elements in the queue. 

def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        tempQueue= q()
        tempQueue.enqueue(rootNode)
        while not tempQueue.isEmpty():
            currentNode= tempQueue.dequeue()
            print(currentNode.data)
            if currentNode.leftChild is not None:
                tempQueue.enqueue(currentNode.leftChild)
            if currentNode.rightChild is not None:
                tempQueue.enqueue(currentNode.rightChild)

print("Level Order Traversal")
levelOrderTraversal(rootNode)


# This is the code for Sraching a node in the tree. 
# There are 2 ways we can use One of the DFS based traversals or BFS based traversals which is queue based. 
# Recommended is BFS since it is a queue based approach. But we are going to try both.

# Here we will use pre order traversal for finding the node. 
def preOrderTraversalSearchVal(rootNode, nodeValue):
    if not rootNode:
        return
    elif rootNode.data == nodeValue:
        return "Value Present"
    else:
        flagValue= preOrderTraversalSearchVal(rootNode.leftChild, nodeValue)
        if flagValue== "Value Present":
            return "Value Present"
        flagValue= preOrderTraversalSearchVal(rootNode.rightChild, nodeValue)
        if flagValue== "Value Present":
            return "Value Present"
    return "Value Not Present"

print("Searching for the Value DFS Way")
print(preOrderTraversalSearchVal(rootNode, "Drinks"))
print(preOrderTraversalSearchVal(rootNode, "Coffee"))


# Here we will try to implement he BFS way of searching the value. For this we will use the Queue DS used in the Level Order traversal.

def levelOrderTraversalSearchVal(rootNode, nodeValue):
    if not rootNode:
        return
    else:
        currentQueue= q()
        currentQueue.enqueue(rootNode)
        while not currentQueue.isEmpty():
            currentNode = currentQueue.dequeue()
            if currentNode.data == nodeValue:
                return "Value Present"
            # Add the nodes to the queue
            if currentNode.leftChild is not None:
                currentQueue.enqueue(currentNode.leftChild)
            if currentNode.rightChild is not None:
                currentQueue.enqueue(currentNode.rightChild)
        
        return "Value Not Present"

print("Searching for the value BFS Way")
print(levelOrderTraversalSearchVal(rootNode, "Hot"))
print(levelOrderTraversalSearchVal(rootNode, "Tea"))



# Here we will implement the code for inserting an element into binary tree. 
# Here I will implement the BFS way of implementing the BT where we do the level order search.

def insertNode(rootNode, nodeValue):
    if rootNode is None:
        rootNode= TreeNode(nodeValue)
        print("Value Inserted at RootNode")
        return
    # If the root node is not none
    # Create a queue DS and insert root node into it.
    tempQueue= q()
    tempQueue.enqueue(rootNode)
    # Loop till the queue has some elements.
    while not tempQueue.isEmpty():
        currentNode = tempQueue.dequeue()
        if currentNode.leftChild is None:
            currentNode.leftChild= TreeNode(nodeValue)
            print("Value inserted as left child")
            return
        else:
            tempQueue.enqueue(currentNode.leftChild)
        
        if currentNode.rightChild is None:
            currentNode.rightChild= TreeNode(nodeValue)
            print("Value inserted as right child")
            return
        else:
            tempQueue.enqueue(currentNode.rightChild)

print("Inserting Value")
insertNode(rootNode, "Pepsi")
insertNode(rootNode, "Cola")
levelOrderTraversal(rootNode)


'''
Next is code to delete the Binary Tree
Here the approach that I need to follow is 
    - First get the deepest node in the tree. 
    - Then replace the value of the deepest node in the tree with the value we want to delete.
    - Then delete the deepest node.

    We will write separate methods to get the deepest node and then delete it.
'''


# Here the logic is, we do the level order traversal and the node at the end is the deepest node. 
def getDeepestNode(rootNode):
    if rootNode is None:
        return 
    tempQueue= q()
    tempQueue.enqueue(rootNode)
    while not tempQueue.isEmpty():
        temp= tempQueue.dequeue()
        if temp.leftChild:
            tempQueue.enqueue(temp.leftChild)
        
        if temp.rightChild:
            tempQueue.enqueue(temp.rightChild)
    
    return temp


# Here I am planning to delete the deepest node:
# This method will take rootnode and the deepest Node. i.e reference to both
# We will again do the level order traversal and once we reach the deepest node, we will set the reference to None.

def delDeepestNode(rootNode, dNode):
    if rootNode is None:
        return 
    tempQueue= q()
    tempQueue.enqueue(rootNode)
    while not tempQueue.isEmpty():
        currentNode= tempQueue.dequeue()
        if currentNode== dNode:
            currentNode= None
            return
        if currentNode.leftChild:
            if currentNode.leftChild== dNode:
                currentNode.leftChild= None
                return
            else:
                tempQueue.enqueue(currentNode.leftChild)
        if currentNode.rightChild:
            if currentNode.rightChild== dNode:
                currentNode.rightChild= None
                return
            else:
                tempQueue.enqueue(currentNode.rightChild)
    

# Here in this method I will actually delete the node. 
# What I want to do is, 
#   - Get the reference to the deepest Node
#   - Then perform the level order traversal to find the node.
#   - Then once the node to be deleted is found, replace the current node with the deepest node.
#   - Once that is done, Delete the deepest node.

def delNode(rootNode, nodeValue):
    pass


# Code to delete the entire binary tree.

def delBinaryTree(rootNode):
    pass
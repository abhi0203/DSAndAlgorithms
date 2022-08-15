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

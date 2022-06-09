'''
Code to create a Binary tree using Linked List method. 
Here we will mainly create the tree node and then will attach the node manually. 
Since this is a binary tree, each node will only have 2 child nodes named left and right.

We will also implement the Pre Order, Inorder and Post order traversal.

'''

from re import L
from tkinter.tix import Tree


class TreeNode:
    def __init__(self, value):
        self.value= value
        self.left= None
        self.right= None


root= TreeNode("Drinks")
hot= TreeNode("Hot")
cold= TreeNode("Cold")
tea= TreeNode("Tea")
coffee= TreeNode("Coffee")
root.left= hot
root.right= cold
hot.left= tea
hot.right= coffee

# Code for PreOrder traversal
# Here the sequence is Center Left right
print("********************************")
print("Pre Order Traversal")
def preOrderTraversal(treeNode):
    if not treeNode:
        return
    print(treeNode.value)
    preOrderTraversal(treeNode.left)
    preOrderTraversal(treeNode.right) 


preOrderTraversal(root)


# Code Inorder traversal
# The path is Left center right
print("********************************")
print("Inorder Traversal")
def inOrderTraversal(treeNode):
    if not treeNode:
        return
    inOrderTraversal(treeNode.left)
    print(treeNode.value)
    inOrderTraversal(treeNode.right)

inOrderTraversal(root)


# Code for post order Traversal
# The path is Left, right center
print("********************************")
print("Post Order Traversal")
def postOrderTraversal(treeNode):
    if not treeNode:
        return
    postOrderTraversal(treeNode.left)
    postOrderTraversal(treeNode.right)
    print(treeNode.value)


postOrderTraversal(root)


'''
Level Order Traversal
This is similar to Breadth Frist Search. In this case, we will use the queue data structure. 
Steps:
- Check if the tree node is none or not. If it is then return. Else continue 
- Insert the root node into the queue. 
- Dequuw from the quee the first element. 
- Print its valuye. 
- Then check if the node has left child. iF it has, then insert the left child into the queue.
- Similarly check if the node has right tree and if it does, then add that as well to the queue. 
'''

#Code to create the queue using linked List. 

class Node:
    def __init__(self, value):
        self.value= value
        self.next= None

class LinkedList:
    def __init__(self):
        self.head= None
        self.tail= None

class Queue:
    def __init__(self):
        self.queue= LinkedList()
    
    def isEmpty(self):
        if self.queue.head== None:
            return True
        else:
            return False
    
    def enqueue(self, value):
        queueNode= Node(value)
        if self.queue.head== None:
            self.queue.head= queueNode
            self.queue.tail= queueNode
        else:
            self.queue.tail.next= queueNode
            self.queue.tail= queueNode

    def dequeue(self):
        if self.queue.head== None:
            print("Queue is empty")
            return None
        returnNode= self.queue.head
        if self.queue.head== self.queue.tail:
            self.queue.head= None
            self.queue.tail= None
        else:
            self.queue.head= self.queue.head.next
        return returnNode.value

# Create the code for Level Order Traversal

print("********************************")
print("Level Order Traversal")
def levelOrderTraversal(treeNode):
    if treeNode is None:
        return
    lotQueue= Queue()
    lotQueue.enqueue(treeNode)
    while not lotQueue.isEmpty():
        node= lotQueue.dequeue()
        print(node.value)
        if node.left:
            lotQueue.enqueue(node.left)
        if node.right:
            lotQueue.enqueue(node.right)


levelOrderTraversal(root)


# Searching an element,
# To search, we can use any of the traversals. 
# However, pre-order (Center, left, right), inorder (left, center right) and postorder (left, right, center) all uses stack and only level order uses queues.
# Since queues perform better than stacks, we use level order search. 

print("*******************************")
print("Searching an Item")
def searchItem(treeNode, searchValue):
    if treeNode is None:
        return "Failure"
    lotQueue= Queue()
    lotQueue.enqueue(treeNode)
    while not lotQueue.isEmpty():
        queueNode= lotQueue.dequeue()
        if queueNode.value == searchValue:
            return "Success"
        if queueNode.left:
            lotQueue.enqueue(queueNode.left)
        if queueNode.right:
            lotQueue.enqueue(queueNode.right)
    
    return "Failure"


print(searchItem(root,"Tea"))
print(searchItem(root,"Cola"))


# INserting a node into the Binary tree.
# Here we again do the Level order search and the place where we find that there no child, we will place the new node there.

print("********************************")
print("Insert Into Node")

def insertNodeIntoTree(root, newNode):
    if root is None:
        root= newNode
        return root
    lotQueue= Queue()
    lotQueue.enqueue(root)
    while not lotQueue.isEmpty():
        node= lotQueue.dequeue()
        if node.left is None:
            node.left= newNode
            return "Node Entered Left"
        else:
            lotQueue.enqueue(node.left)
        if node.right is None:
            node.right= newNode
            return "Node Entered Right"
        else:
            lotQueue.enqueue(node.right)
    


cola= TreeNode("Cola")

print(insertNodeIntoTree(root, cola))
levelOrderTraversal(root)


# Deleting a Node
# The logic here is to Find the right most or the deepest node in the tree. 
# Then replace the value in that node with the value that we want to delete.
# ONce that is done, delete the last most node. 

print("********************************")
print("Find Deepest Node")
# We simply do the level order search again and then return the reference to the final node. 
def findDeepestNode(root):
    if root is None:
        return
    lotQueue= Queue()
    lotQueue.enqueue(root)

    while not lotQueue.isEmpty():
        node= lotQueue.dequeue()
        if node.left:
            lotQueue.enqueue(node.left)
        if node.right:
            lotQueue.enqueue(node.right)
    
    deepNode= node
    return deepNode

deepNode= findDeepestNode(root)
print("Deepest Node")
print(deepNode.value)


def findNodeToBeDeleted(treeRoot, node):
    if treeRoot is None:
        return None
    if treeRoot== node:
        return treeRoot
    elif treeRoot.left is None and treeRoot.right is None:
        return None
    else:
        lotQueue= Queue()
        lotQueue.enqueue(treeRoot)
        while not lotQueue.isEmpty():
            currentNode= lotQueue.dequeue()
            if currentNode.left== node:
                print("Node to be deleted")
                print(currentNode.left.value)
                return currentNode.left
            else:
                lotQueue.enqueue(currentNode.left)
            if currentNode.right== node:
                print("Node to be deleted")
                print(currentNode.right.value)
                return currentNode.right
            else:
                lotQueue.enqueue(currentNode.right)
        return None




def deleteDeepestNode(treeRoot, deepestNode):
    lotQueue= Queue()
    lotQueue.enqueue(treeRoot)
    while not lotQueue.isEmpty():
        currentNode= lotQueue.dequeue()
        print(currentNode.value)
        if currentNode.left== deepestNode:
            currentNode.left= None
            return
        else:
            lotQueue.enqueue(currentNode.left)
        if currentNode.right== deepestNode:
            currentNode.right= None
            return
        else:
            lotQueue.enqueue(currentNode.right)
    return
            


# Now combine the 2 methods, to do the replacement and replace the node.
# Cases,
# 1. Tree is empty
# 2. Only one node in the tree and that is to be deleted.
# 3. More than one Node in the tree and root to be deleted.
# 4. More than one node in the tree and non root to be deleted. 
# 5. Node to be deleted is not present.

def doNodeReplacement(treeRoot, node):
    if treeRoot is None:
        return "Cant Delete Node. Tree is empty"
    
    deepestNode= findDeepestNode(treeRoot)
    nodeToBeDeleted= findNodeToBeDeleted(treeRoot, node)

    if nodeToBeDeleted is None:
        return "Node cannot be deleted. Either not present"
    elif treeRoot.left is None and treeRoot.right is None and treeRoot== nodeToBeDeleted:
        treeRoot= None
        return "Only one node and that is deleted."
    elif treeRoot== nodeToBeDeleted:
        treeRoot.value, deepestNode.value= deepestNode.value, treeRoot.value
        deleteDeepestNode(treeRoot, deepestNode)
    else:
        lotQueue= Queue()
        lotQueue.enqueue(treeRoot)
        while not lotQueue.isEmpty():
            currentNode= lotQueue.dequeue()
            if currentNode.left== nodeToBeDeleted:
                currentNode.left.value, deepestNode.value= deepestNode.value, currentNode.left.value
                deleteDeepestNode(treeRoot, deepestNode)
                return "Node is deleted"
            else:
                lotQueue.enqueue(currentNode.left)
            if currentNode.right== nodeToBeDeleted:
                currentNode.right.value, deepestNode.value= deepestNode.value, currentNode.right.value
                deleteDeepestNode(treeRoot, deepestNode)
                return "Node is deleted"
            else:
                lotQueue.enqueue(currentNode.right)

print("***************************")

print(doNodeReplacement(root,root))


print("********************************")
print("Level Order Traversal")
levelOrderTraversal(root)






'''
This code is to create a binary tree using Python list. 
Here in this case, the formula we use to treat a list as binary tree is 
- We mark the first element of the tree as None. We leave it as that for simplicity of the calculation purpose.
- We then start with second index or index 1 and use the formula leftNode = 2n and rightNode= 2n+1 where n is the index of the parent/ root node for the 2 child nodes


'''

class BinaryTree:
    # Here we define the self and maxsize variable. 
    # In order to keep insert operations at sane level, we are limiting the size of the tree.

    def __init__(self, maxSize):
        self.treeList= maxSize * [None]
        self.currentNode= 0
        self.size= maxSize

    # Here in this case, we are simply inserting the node at the next index in the list.
    # HOwever, based on the logic of 2n and 2n+1 we are using, when it comes to tree traversal, it will come as if we are retrieving the 
    # Algo
    # Check if the list is full. If it is return the tree full message
    # Else add the element to the next item in the list and move on.
    def insertNode(self, value):
        if self.currentNode+ 1== self.size:
            return "Tree is Full"
        self.treeList[self.currentNode+1]= value
        self.currentNode+=1
        return "Node is inserted"


listTree= BinaryTree(4)
print(listTree.insertNode("Drinks"))
print(listTree.insertNode("Hot"))
print(listTree.insertNode("Cold"))
print(listTree.insertNode("Tea"))
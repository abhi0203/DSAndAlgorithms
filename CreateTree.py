# Code to create a basic tree.
# Here I am creating a node in the class tree node and each node has a value and list. 
# The list represents the children. Since it is a tree with one node having many children, we are using the list to represent the children.
# For a binary tree, we can simply use 2 pointers left and right. 
# Cons here is, we just cant have direct pointer to the children. We have to go through a indexing of the python list.

class TreeNode:
    def __init__(self, value, children=[]):
        self.value= value
        self.children= children
    

    def __str__(self, level=0):
        ret= " "* level + str(self.value) + "\n"
        for child in self.children:
            ret+= child.__str__(level+1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)



drink= TreeNode("Drinks",[])
hot= TreeNode("Hot",[])
cold= TreeNode("Cold",[])

drink.addChild(hot)
drink.addChild(cold)

print(drink)
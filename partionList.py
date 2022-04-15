# Here we want to partion a given list based on an item.
# Eg: 1-> 4->2->3->5 and value is 3
# 1-> 4->2->3->5
# For above list, if value is 3, all the items < 3 should be on the left side and all the items greater than 3 should be on right side.
# We dont need to have things sorted.
# Its okay if we have a solution like 1->2->4->3->5.

# Option 1:
# Start with first node.
# If it is greater than or equal to the value, 
# - create a new node and append at the tail.
# - Delete this node.
# Else if it is less than value, 
# - create a new Node and append at the head
# - delete this node.
# This way we can do things on O(n) time complexity and space complexity is O(1)
# It is slightly difficult as we are adding values to the end of the list.
#

from LinkedList import LinkedList, Node

#Time complexity for above list is O(n) but spacen complexity is also O(n)
# Also this solution does not maintain the sequence in which the nodes appear in first list. 

def partitionList(lla, x):
    if lla.head is None:
        print("List is empty. returning None")
        return None
   
    # 1 2->3->4   3 
    # 1->2->3->4-None  (2)->1

    prevNode= lla.head
    currentNode= lla.head
    while currentNode: 
        if lla.head is lla.tail:
            # there is only one item in the list. Nothing cna be done. return list
            return lla
        else:
            llb= LinkedList()
            currentNode= lla.head
            llb.add(currentNode.value)
            while currentNode.next:
                currentNode= currentNode.next
                if currentNode.value<x:
                    node= Node(currentNode.value)
                    node.next= llb.head
                    llb.head= node
                else:
                    node= Node(currentNode.value)
                    llb.tail.next= node
                    llb.tail= node
        return llb
        # 1->5->3->6->2->None  4
        # 2->3->1->5->6->Nonde

# Solution to do the partiotion in place and with O(N)
# List is nothing but 
# Nodes that are stitched together and 2 pointers head and tail
# This means, if we create an object of Node class, we should be able to do all the operations that we do on list.
# Note head and tail are just pointers in list class. Deep down its nodes.
# Here in this option, we are using an empty node for our purpose which gives us initial pointers. from there we can do anything.

# Approach 2:
# Create 2 dummy nodes. One node represent the left side other node should represent the right side.
# Start going through each node of the main linked list
# If the value is less than the partition numbers, point the left node's next to that node.
# If the value is greater than or equal to the point the right side node's next to that node. 
# At the end of the list, left side node's next should be pointing to right side node's first element.
# At the end, last node on right side node's pointer should be pointing to None.

def partitionList2(lla, x):
    leftNode= Node()
    rightNode= Node()

    leftNodeTail= leftNode
    rightNodeTail= rightNode

    currentNode= lla.head

    if not currentNode:
        print("List is empty. Returning None")
        return None
    
    while currentNode:
        if currentNode.value < x:
            leftNodeTail.next= currentNode
            leftNodeTail= currentNode
        else:
            rightNodeTail.next= currentNode
            rightNodeTail= currentNode
        
        currentNode= currentNode.next
    
    leftNodeTail.next= rightNode.next
    rightNodeTail.next= None

    lla.head= leftNode.next
    lla.tail= rightNodeTail

    return lla
    



lla= LinkedList()
lla.generate(2,0,10)
print("Original List")
print(lla)
print("Partition 1")
print(partitionList(lla, 7))
print("Partition 2")
print(partitionList2(lla,7))





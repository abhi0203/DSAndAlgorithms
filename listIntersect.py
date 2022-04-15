# This method is used to check if 2 lists intersects. 
# 2 lists intersect if there is a common node that 2 or more lists have.
# 

# Logic
# List can be of varying length.
# First let us find the length of the both lists.
# Then we find the difference.
# Then we find the longer list and move the current node of that list by the difference we calculated above.
# Once we move by the offset, we now know that both lists are of same length and we can move both of them simultaneously.
# We then check if the tow pointers points to the same node and if they do, we return a reference to that node (or value)
# If we reach end and none of the lists points to same node, we return NOne
# 
from LinkedList import LinkedList, Node
from random import randint

def listIntersect(lla, llb):
    #Check if any of the lists is empty. If it is, there cant be an intersection.
    if lla.head is None or llb.head is None:
        print("One of the node is empty. returning None.")
        return None
    
    lengthA= len(lla)
    lengthB= len(llb)
    greaterA= True

    # Find which list is bigger
    if lengthA>= lengthB:
        offset= lengthA- lengthB
    else:
        offset= lengthB- lengthA
        greaterA= False

    currentNodeA= lla.head
    currentNodeB= llb.head

    # Move the bigger list by offset
    if greaterA:
        for i in range(offset):
            currentNodeA= currentNodeA.next
    else:
        for i in range(offset):
            for i in range(offset):
                currentNodeB= currentNodeB.next
    
    while currentNodeA and currentNodeB:
        if currentNodeA== currentNodeB:
            print("List Intersect at below node.")
            return currentNodeA.value
        currentNodeA= currentNodeA.next
        currentNodeB= currentNodeB.next
    
    print("None of the list have a commone Node. ghence no intersection")
    return None


def createIntersection(lla, llb):
    if lla.head is None or llb.head is None:
        print("One of the list is empty")
        return None
    newNode= Node(randint(0,9))
    lla.tail.next= newNode
    lla.tail= newNode

    llb.tail.next= newNode
    llb.tail= newNode


lla= LinkedList()
llb= LinkedList()

#lla.generate(5,0,99)
llb.generate(5,0,99)

print("Node A before the intersection")
print(lla)

print("Node B before intersection")
print(llb)

#createIntersection(lla, llb)
#createIntersection(lla, llb)
#createIntersection(lla, llb)

print("List A after intersection")
print(lla)

print("List B after intersection")
print(llb)


print(listIntersect(lla,llb))




    

    

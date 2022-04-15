# This method removes the duplicates from a singly linked list
# There are 2 ways we can do this and I am truing to implement both ways.

# Option 1":
# giving up on space to get better performance.
# - create an empty set
# - Go through the list item one by one.
# - check if the item is present in the set
#   - if it is present, then remove that item from the list
#   - else add the item value in the set
# - Iterate till we go to the last element of the list.

from LinkedList import LinkedList

# In this method, I am using a set. So space complexity becomes O(n)
# Since we are just going through the list once it is O(n) time complexity and the in operator on set is O(1). So overall time complexity is O(n)

def removeDups(llA):
    # Check if the list is empty
    if llA.head is None:
        print("List is empty.")
        return None
    else:
        # 1->2->3->3->4->5->None {1,2,3,4,5}
        prevNode= None
        currentNode= llA.head
        tempSet=set()
        while currentNode:
            if currentNode.value in tempSet:
                # Code to remove the node from the list
                prevNode.next= currentNode.next
                currentNode.next= None
                currentNode= prevNode
            else:
                # Code to add the value into the set
                tempSet.add(currentNode.value)
            
            prevNode= currentNode
            currentNode= currentNode.next
    
    return llA

# Here we will try to do the de-duplication in place
    # So insted of creating a new list, we will go from the list twice comparing each item to every other item
    # The time complexity will be O(n^2) as we are comparing every item of the list with every other item.
    # Algorithm
    # 
    #   - Set a temp variable to the first node in the list.
    #   - Start the outer loop till the node is not none.
    #       - set second temp variable to to current vairbale's next. 
    #       - start second loop with second  temp variable till seconde node is not none.
    #       - Each iteration, compare the value of inner node with value of outer node.
    #           - if the value is equal, delete that node.
    #           - else move to new node.
    #   - At the end, return the list. 

def removeDups2(llb):
    if llb.head is None:
        print("the list is empty")
        return None   
    else:
        currentNode= llb.head
        while currentNode:
            # 1-> 2-> 3-> 3-> 4-> None
            prevNode= currentNode
            nextNode= currentNode.next
            while nextNode:
                if currentNode.value== nextNode.value:
                    prevNode.next= nextNode.next.next
                    nextNode.next= None
                    nextNode= prevNode.next
                else:
                    prevNode= nextNode
                    nextNode= nextNode.next
            
            currentNode= currentNode.next
        
        return llb

llA= LinkedList()

print("First method with extra space")
llA.generate(10,0,5)
print(llA)
print(removeDups(llA))

llb= LinkedList()
print("Second method with extra time")
llb.generate(10,0,5)
print(llb)
print(removeDups(llb))
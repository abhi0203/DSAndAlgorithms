
# In this problem we need to return the value of kth element from the last node.
# There are multiple ways we can do this. 
# We assume that k will always be positive.
# We also assume that if k is greater than length of the list, we mark it as invalid case.

# Option 1:
# - Create a new list. The traverse from first list all the way and add the value from every single node of first list as head of new list.
# - we then travel k element in the new list and return the value. 
# This code is not that optimal but gets the job done at the cost of O(kn) time complexity and O(n) space complexity.

# Option 2:
# Second option is to use 2 pointers. 
# First step, both pointers start at head.
# We then move the second pointer to k locations.
# So the difference between first and second pointer is K.
# We then move both pointers together one step till the second pointer reaches the end of the list.
# We then return the value pointed by first pointer. 
# This code should be O(n) for time complexity and O(1) for space complexity

from LinkedList import LinkedList

def returnKthLastElement(lla, k):
    if lla.head is None:
        print("List is empty. Returning None")
        return None
    
    firstPointer= lla.head
    secondPointer= lla.head
    # 1->2->3-None   0,1,2
    for i in range(k):
        secondPointer= secondPointer.next
        if not secondPointer:
            if i+1== k:
                break
            else:
                print("K is greater than list len. Invalid case. Returning None")
                return None
    
    while secondPointer:
        firstPointer= firstPointer.next
        secondPointer= secondPointer.next

    return firstPointer.value

lla= LinkedList()
lla.generate(10, 0, 100)
print(lla)

print(returnKthLastElement(lla, 11))

# This method takes 2 lists and returns their sum.
# every digit is represented by a value in the node.
# The head represent the digit at unit place and so on.
# Both the lists can be of any length.
# If one of the list is emoty, the sum list should be same as other list
# If both the lists are emoty, then we should display the None.


from LinkedList import LinkedList, Node

def sumList(lla, llb):
    # Logic to check if any or both the lists are None
    if lla.head is None and llb.head is None:
        print("The list is empty")
        return None
    elif lla.head is None:
        return llb
    elif llb.head is None:
        return lla
    sum= 0
    carry= 0
    # Logic:
    # Start with the first item from both the lists 
    # Access their value and sum them.
    # Use modulo 10 to calculate number in node
    # Use div to calculate carry 
    # Reset sum and carry to 0 at right time.
    # Create a new Node with the sum varaible and assign it to the third linked list.
    # Move to the next item.
    # Loop until both the lists are empty. If one of the list is empty, just appent all the values from other list.

    currentNodeA= lla.head
    currentNodeB= llb.head
    llc= LinkedList()

    while True:
        # If both the nodes are none then break
        if currentNodeA is None and currentNodeB is None:
            break
        # If one node is none use 0 as value for sum. Else get the value of current ndoe and move pointer to next
        if currentNodeA is None:
            aVal=0
        else:
            aVal= currentNodeA.value #7
            currentNodeA= currentNodeA.next

        if currentNodeB is None:
            bVal= 0
        else:
            bVal= currentNodeB.value #0
            currentNodeB= currentNodeB.next

        sum= aVal + bVal + carry  # 8
        num= sum % 10 #8
        carry= int(sum/10) #0
        llc.add(num)  # 5->1->3->8  
    
    if carry>0:
        llc.add(carry) #None

    return llc


lla= LinkedList()
llb= LinkedList()

lla.generate(4,0,9)
print("LLa is as below")
print(lla)
llb.generate(3,0,9)
print("LLb is as below")
print(llb)

print("Sum is ")
print(sumList(lla, llb))



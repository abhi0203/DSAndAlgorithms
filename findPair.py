def pairSum(myList, sum):
    # TODO
    # Create and empty list
    # Start with first item. Go all the way from second element to last
    # and sum it with first element. If the sum matches, add it in the new list as string
    # Else continue.
    # O(n^2)
    newList=[]
    for i in range (len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i]+myList[j]==sum:
                newList.append(str(myList[i])+'+'+str(myList[j]))
    
    return newList


print(pairSum([2,4,3,5,6,-2,4,7,8,9],8))
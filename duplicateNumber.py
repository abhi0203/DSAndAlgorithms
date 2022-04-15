# Assumes that the list is sorted.
# If the list is not sorted, then either sort the list, or it will be O(n^2)
def removeDuplicates(myList):
    if myList==[]:
        return None
    secondList=[]
    temp= None
    for i in range(len(myList)):
        if myList[i]!=temp:
            secondList.append(myList[i])
            temp= myList[i]
    
    return secondList

print(removeDuplicates([1,1,1,2,2,3,4,1,4]))


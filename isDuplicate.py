'''

Need to find all the element are unique in the list. The function should return True or False.

Eg:
[1,2,3,4,5] True

[2,2,3,4,5,6] False

Test Case:
- For empty list, return None.
- Okay to have -ve or positive number.
- Should we print all duplicate numbers or just the first one?

Approach 1:

- Start with first item. 
- Compare it with remaining all. 
- If duplicate found return True. Else False


Time Complexit is O(n^2)

Approach 2:

- Sort the array with quick sort. This is O(nlogn) operation.
- The traverse through the array once and compare the number to next number. O(n)
- If duplicate return True

Approach 3:
- Create and hashmap
- start adding the numbers as key
- If the key is present, return True.

Space complexity is O(n)
Time complexity is O(n)

'''

def isDuplicate(myList):
	if myList==[]:
		return None

	listDict={}
	for i in myList:
		if i in listDict.keys():
			print(i)
			return True
		else:
			listDict[i]=1

	return False


print(isDuplicate([1,2,3,4,5,6,7,8,8]))

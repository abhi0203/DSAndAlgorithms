'''
Given an unsorted array, find the max product of 2 numbers.
'''


'''
Example:

[2,3,5,1,21,43,56,22,5] Answer is 56*43 =2408

[2,4,1,5,7,6]
'''

'''
Questions:
- Can it contain positve and negarive numbers?
- What should we do when the arry is repeated?
- Can it contain duplicate numbers?
- Should we consider multiplying same number with itself again?
'''

'''
Approach 1:

- Create a variable called answer=0
- Start with 1st element. Multiply it with all the elements in the array one by one.
	- Compare the answer of the multiplication with answer variable. If greater replace.
	- Else Continue
- Finally return the answer
 
 Time Complexity: O(n^2) as we have to go through the array twice in a loop.

 Approach 2: 

 - Sort the array using quick sort or merge sort. 
 Time complexity of the sort would be O(nlogn)

 Then take the last 2 elements and calculate the multiplication. This should be O(1)


 I am going to take approach 1
 '''

def maxProduct(myList):
 	answer= 0
 	if myList==[]:
 		return None

 	for i in range(len(myList)):
 		for j in range(i+1, len(myList)):
 			if myList[i]*myList[j] > answer:
 				answer= myList[i]*myList[j]

 	return answer


print(maxProduct([2,3,5,1,21,-43,56,22,5]))

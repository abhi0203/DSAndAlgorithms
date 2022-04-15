
#Code to find sum of two numbres in an array that equals given numbres

def twoSum(myArray, target):
	print("Into 2 sum")
	if myArray==[]:
		return None
	for i in range(0, len(myArray)):
		for j in range(i+1, len(myArray)):
			if myArray[i]+myArray[j]==target:
				print(i,  j)




def twoSumBetter(myArray, target):
	print("into two sum better")
	leftPointer= 0
	rightPointer= len(myArray)-1

	if myArray==[]:
		return None

	while leftPointer <=rightPointer:
		if myArray[leftPointer]+ myArray[rightPointer]== target:
			print(leftPointer, rightPointer)
			return
		elif myArray[leftPointer]+ myArray[rightPointer]< target:
			leftPointer+=1
		else:
			rightPointer-=1


twoSum([1,2,3,4,2,3,4,5,6], 10)
twoSumBetter([1,2,3,4,2,3,4,5,6], -10)
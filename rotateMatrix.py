
'''

Given the N*N matrix rotate the same by 90 degree. i.e. first row becomes third column.

Eg:

 1  2  3 10         7 4 1 
 4  5  6 11   =>    8 5 2
 7  8  9 12         9 6 3
13 14 15 16
Questions:

- Always a square matrix
- Always needs to be rotated by 90degredd
- Should not be used with second matrix

Appraoch:
a[0][0] -> a[0][-1]
a[0][-1] -> a[-1][-1]
a[-1][-1] -> a[-1][0]
a[-1][0] -> a[0][0]

i =0 j= n

Logic:

- Since we have to do this in memory, this should take O(n^2)
- Assume we have a metrics with layers.
- So we go for the outermost layer first and then go on to inner most layers till we are left with one element.
- For outermost layer, we start from first element and keep on moving until last but one element.
	- For each cycle we replace the position of the element relative to start and end location.
	- Once we are done with one cycle we move to the next element in the same layer and so on.
- Once we are done with one layer, we move to the inner layer relative to the position of the outer layer and repeat above loop.

'''

import numpy as np

def rotateMatrix(myArray):
	n= len(myArray)
	#How many layers will be defined by taking absolute diviosn
	# For eg: 3x3 matrix will have 3//2= 1 layer to rotate. 4x4 matrix will have 4//2 =2 matrix to rotate and so on.
	for layer in range(n//2):
		#For that layer, define the first and last element so that we can rotate through them
		first = layer
		# last should be one less that last element of the array. So it can be taken from layer
		last = n-layer-1
		# Rotate from first to last, and in each iteration, replace the values of the corners
		for i in range(first, last):
			# Save the first element in temp variable
			temp= myArray[layer][i]

			# Replace top with left

			myArray[layer][i]= myArray[-i-1][layer]

			# Replace left with bottom
			myArray[-i-1][layer] = myArray[-layer-1][-i-1]

			#Replace bottom with right
			myArray[-layer-1][-i-1]= myArray[i][-layer-1]

			# replace right with temp
			myArray[i][-layer-1]= temp
	return myArray

myArray= np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

print(myArray)

print("After Rotation")


print(rotateMatrix(myArray))















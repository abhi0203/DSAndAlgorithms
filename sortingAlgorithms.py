

"""'''
THis is the code for bubble sort.
In this case, this is the most basic algorithm for sorrting.
This is an algorithm which is in place sorting algorithm,
Also this is an algorithm which is stable type of algorithm.
In this case, every element in the array gets compared with every other element in the array and finally at the end of every single iteration, one element bubbles up in its right sorted position.

Assuming we are sorting in ascending order, 

The way it works is, we start with the first element. We compare it with the next element. 
If the current element is greater than the next element, we swap. 
Else we move to the next element. 
We iterate it again and agin for every single number in the list. 
At the end of the loop, we have sorted list.
'''
"""

from pydoc import cli
import math


def bubbleSort(cList):
    if cList ==[]:
        return cList
    print("Bubble Sort")
    for i in range(len(cList)-1):
        # The reason we create range for one less is because we are going to refer the i+1 during the comparison. Else, we can start with 1 instead of 0.
        for j in range(len(cList)-1):
            if cList[j]> cList[j+1]:
                cList[j], cList[j+1]= cList[j+1], cList[j]
    
    print(cList)


bubbleSort([2,3,1,5])


"""
In the basic case, we are repeating the traversal till last element again and again. 
We can minimize the same in the second loop by 1 for each iteration.
This can be done by subtracting i value inside the range function.
"""

def bubbleSortOpt(cList1):
    print("Bubble sort Optimized")
    for i in range(len(cList1)-1):
        for j in range(len(cList1)-i-1):
            if cList1[j]> cList1[j+1]:
                cList1[j], cList1[j+1]= cList1[j+1], cList1[j]

    print(cList1)


bubbleSortOpt([2,3,1,5])

# Time complexity is O(n^2) and space is O(1)


"""
Selection Sort
- This sort is similar to that of the bubble sort, in the sense, it also uses 2 loops. 
- It is similar to bubble sort where in at the end of each loop, one element is in the sortted position.
- Here the logic is, we logically split the arry into sorted and unsorted portion.
- Initially the sorted portion is 0 and entire array is considered as unsorted. 
- We then assume that the first index element is sorted. 
- We then move from second element till the last and if we find any element smaller than that of current index, we make the smallest index as that element. 
- At the end, we swap the current value (which is pointing to first element in the loop) with the minimum index and move the current elment to the next value. 

Difference from the bubble sort.
- In the bubble sort, we swap multiple times. In the selection sort, we just swap once at the end. 

"""

def selectioSort(cList):
    if cList ==[]:
        return []
    print("Selection Sort")
    for i in range(len(cList)):
        current_min_index= i
        for j in range(i+1, len(cList)):
            if cList[j] < cList[current_min_index]:
                current_min_index= j
        #Finally when we are outside the loop, we swap i vale with current min index value and this way we get the element in the sorted position.
        # Also, as i moves further, we move to the next element automatically.
        cList[i], cList[current_min_index]= cList[current_min_index], cList[i]
    
    print(cList)

selectioSort([2,3,1,5])


"""
Insertion Sort

- This sort takes the logic from Selection sort further.
- In the selection sort, we use the logic of sorted vs unsorted array and then change the swap the position of the array element.
- in the insertion sort, we still use the logic of sorted vs unsorted array, but in this case, we actually insert the current array element into the sorted portion of the array instead of swapping.
- An array with one element is considered as sorted.
- So we start with the second element. 
- Now in the second element, we start with the last element in the sorted array and finally, insert that element at the right position in the sorted array by moving all the elements.
- We then move to the next elements.

Time complexity is O(n^2) and space complexity is O(1)

"""

def insertionSort(cList):
    if cList== [] or len(cList)==1:
        return cList
    print("Insertion Sort")
    # Start the for loope from second element as we are assuming that first element is sorted.
    for i in range(1, len(cList)):
        # Create an element j which represents the sorted array and assign it to i-1 so that as i increases, the value of j also increases.
        j = i-1
        currentElement= cList[i]
        # Next step is the compare the current element pointed by i with all the elements from j till 0th position and if the current element is less than element pointed by j, we just the move the current element to the next place. 
        while j >=0 and cList[j]> currentElement:
            cList[j+1]= cList[j]
            j-=1
        # Finally we have reached a place where either j is at 0 or j points to an element which is the right position for element pointed by i
        cList[j+1]= currentElement
    return cList


insertionSort([1,3,2,0,5,4,7,6])



"""
Next sort is bucket sort.
The key is, we split the data in what we called as buckets which are nothing but an additional data structure like list of the lists.
First we need to identify how many buckets we need to create. This is done by using the no_of_buckets = round(sqrt(number_of_elements))
Once we have the number of elements we create and array of lists where each list represents an bucket.
We then need to add the elements to the bucket. This is done using formula
ceiling ( value * number of buckets / maxValue)
Using this formula we ensure that values are relatively evenly distributed and values in first bucket are always smaller than the one in second bucket than the one third bucket and so on.

We then use some existing sorting algorithnm on every bucket which can be any one like insertion sort or selection sort. Ideal is quick sort.
Finallu we combine the data from the buckets into one array and return it.

Time complexity is O(nlogn or n^2) based on the type of the algorithm we use for sorting, and space is O(n)
This is used especially when we have know that data is randomly distributed and space is not that big of a concern assuming we are using quick sort
"""
def bucketSort(cList):
    if len(cList) < 2:
        return cList
    # Identify the number of buckets we want to have.
    noOfBuckets= round(math.sqrt(len(cList)))
    # Create buckets
    bucketArray= []
    for i in range(noOfBuckets):
        bucketArray.append([]) 
    # Add elements to the array
    maxElement= max(cList)
    for value in cList:
        bucketNumber= math.ceil((value * noOfBuckets)/ maxElement)
        bucketArray[bucketNumber-1].append(value)
    # Use some sorting algorithm, sort the individual arrays.
    for i in range(noOfBuckets):
        bucketArray[i]= insertionSort(bucketArray[i])
    # Combine the array in to one array
    #finalArray= []
    k= 0
    for i in range(noOfBuckets):
        for j in range(len(bucketArray[i])):
            cList[k]= bucketArray[i][j]
            k+=1
    
    return cList

print(bucketSort([1,3,2,5,4,7,6]))


def quickSort(array):
    # Write your code here.
    #Check if the array is smalle or not.
    if len(array)<2:
        return 
    print("Quick Sort")
    left= 0
    right = len(array)-1
    quickSortHelper(array, left, right)
    return array


def quickSortHelper(array, left, right):
    if left>= right:
        return

    i= left
    j= right-1
    pivot= array[right]

    #While we  i < J, we move the varaibles forward and backworf.
    while i < j:
        #In the inner loop, we move i forweard till it reaches right or array[i]< pivot
        while i< right and array[i]< pivot:
            i+=1
        #In the second inner loop, reduce j till it reaches left or array[j]> pivot
        while j> left and array[j]> pivot:
            j-=1
        #Here if we come out of both the loops, check if i is still less than j and if it is, swap
        if i< j:
            array[i], array[j]= array[j], array[i]

    #Finally we are out of the while loop as at some point i crossed J
    # So we need to check if the current value pointed by i is greater than that of pivot and if it is, then we do one final swap. 
    #If it is not greater than the pivot is the largest element in the subarray coz i have reached left.
    if array[i]> pivot:
        array[i], array[right]= array[right], array[i]

    quickSortHelper(array, left, i-1)
    quickSortHelper(array, i+1, right)

    return
        
        
print(quickSort([1,3,2,5,4,7,6]))
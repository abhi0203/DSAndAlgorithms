"""
The problem statement is
- We have been given N houses along a street with some amount of money in them
- Adjacent houses cannot be stolen
- We have to find the maximum money that can be stolen.

Again, this sounds like a Divide and Conquor type problem as this mentiones a problem where we might have to find all the permutations. 

Since we cannot steal from adjacent houses, that does not mean it will maximize by stealing from alternate houses with maximum money.
So how do we divide this problem?
- So it is mentioned that the robber cannot rob from adjacent offices. 
- And we have to maximize the sum of amouint collected. 
- So what we can do is, we can assume that current house + recurse(index+2) will give us some money. 
- We then get another money from current+1 house + recurse(index+2) and get another set of money.
- We can then return the max of this to the calling function.  
"""

def robHouses(houses, idx):
    if idx>= len(houses):
        return 0
    if idx==len(houses)-1:
        option1= houses[idx]+ robHouses(houses, idx+2)
        return option1
    else:
        option1= houses[idx]+ robHouses(houses, idx+2)
        option2= houses[idx+1] + robHouses(houses, idx+3)
        return max(option1, option2)

print(robHouses([40,5,8,20,30,30], 0))


"""
In this case, we want to use the house robber problem without the recursion.
So one way to do it is, to have an array where we are mentioning the maximum value calculated till that point. 
Eg: [1,2,3,1]
If we create a new array, the first 2 values in the array will be the same. 
Now for the third value, we need to find the max value till current -1 the element and then add the current to it and place it at that index. 
We continues this till we reach the end of the main array. Finally we return the maximum value in the array and that is the amount robber can take. 
[1,2, ]
"""

def robHouseBU(houses):
    if houses==[]:
        return 0
    if len(houses)<=2:
        return max(houses)
    # Create the empty array and we should initialize it to 0
    retArray=[0] * len(houses)
    # Now populate the first 2 element of the new array with first 2 elements of houses.
    retArray[0]= houses[0]
    retArray[1]= houses[1]
    # Now start looping from 3rd element but add only the max
    for i in range(2,len(houses)):
        retArray[i]= houses[i]+ max(retArray[:i-1])
    return max(retArray)

print(robHouseBU([40,5,8,20,30,30]))

# This will go with time complexity O(n^2) and space of O(n)
"""
Another way to optimize it is if we just look at 3rd place, it take max till max till 3-2 place and add. So in above example its
4th place is max till 4-2 + current
5th place is max till 5-2 and current
6th place is max till 6-2 and current
If I see, the max is always the last element and the before the n-1 i.e n-2th element. 
40, 5, 48, 60, 78, 90 

"""
def robHouseBUOpt(houses):
    if houses==[]:
        return 0
    if len(houses)<=2:
        return max(houses)
    # Create the empty array and we should initialize it to 0
    retArray=[0] * len(houses)
    # Now populate the first 2 element of the new array with first 2 elements of houses.
    role1= 0
    role2= 0
    # Now start looping from 3rd element but add only the max
    for i in range(len(houses)):
        temp= max(houses[i]+ role1,role2)
        role1= role2
        role2= temp


    return role2

print(robHouseBUOpt([40,5,8,20,30,30]))

# 40, 5, 48, 48, 78, 78

'''
For the house robber 2 problem, we have to imagine that the houses are in circular part.
So in that case we cant rob from first and last house in the array.
So what we actually need to do is piggy back on house robber one problem.
We do this by first calculating the max with 1 to n-1 house and then from 2 to n house.
Finally we take the max of that.
Max is O(2n) complexity

Another problem is the tree problem.
Here what we need to do is 


'''
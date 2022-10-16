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
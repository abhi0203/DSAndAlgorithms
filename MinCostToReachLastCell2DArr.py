"""
Problem statement:
- A 2D array is given. 
- Each cell has a cost associated with it for accessing the cell.
- we need to start from cell (0,0) and reach till cell (n-1, n-1)
- We can either go only right or mimimum. 
- The condition is cost should be minimum.

Since we are given a 2 D arry, this is relatively simple problem as we can go to right or down. So that gives us how to divide the work.
Finally we calculate the cost for each path and then minimize the by sending the min of 2 upword. 
We are also assured that the there exists atleast one path. 


How can we approach the problem?
- we can start from the end cell and reach to first one or vice a versa.
- We add the cost in the current cell and then recursively call the method with either right or down by incrementing the column and the row value one at a time.
- Since we are calculating the minimum, we should return infinity if the row number or column number increases. That way minimum goes up.
- Also, we need to stop the moment we return the last cell.


Conditions to return are 
- Either row or column is out bounds.
- We have reached the last cell


"""

from cmath import inf


def minCostReachLastCell(matrix, rowNum, colNum):
    if rowNum>= len(matrix) or colNum>=len(matrix[0]):
        return float('inf')
    if rowNum==len(matrix)-1 and colNum==len(matrix[0])-1:
        return matrix[rowNum][colNum]
    else:
        op1= matrix[rowNum][colNum] + minCostReachLastCell(matrix, rowNum + 1, colNum) 
        op2= matrix[rowNum][colNum] + minCostReachLastCell(matrix, rowNum, colNum + 1) 
        return min(op1, op2)


TwoDList = [[4,7,8,6,4],
           [6,7,3,9,2],
           [3,8,1,2,4],
           [7,1,7,3,7],
           [2,9,8,9,3]
           ]

print(minCostReachLastCell(TwoDList, 0, 0))
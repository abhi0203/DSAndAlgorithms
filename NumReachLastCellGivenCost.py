"""
Problem statement

- 2D array is given
- Each cell has a cost associated with it.
- We need to start from cell (0,0) and reach cell (n-1, n-1)
- We can only go right or down from current cell.
- we are given a total cost to reach the cell. 
- We have to find number of ways to reach the last cell using total cost.

Since it is moving along a 2D matrix, we can use Divide and conquor approach. Also we can divide the work with using one path as going right and other as going down.
It is also assumed that there will be atleast one path that get the work done. 

What are the conditions where we need to return? Also, we need a way to manage the cost. 
- First is definitely row or column goiing beyond. (not sure what to return)
- Then if by adding the current cost we go beyond the allocated cost, we can return 0
- If we are at last cell and adding the current cost makes it equal to final cost, we can return 1
- If current cost is less than final cost as we are not at the last cell, we can always move in the divide and conquor world. 
- Finally we combine the ways and return the count.

"""


def reachLastCell(matrix, rowNum, colNum, cost):
    if rowNum>= len(matrix) or colNum>= len(matrix[0]):
        return 0
    if matrix[rowNum][colNum]> cost:
        return 0
    if rowNum== len(matrix)-1 and colNum==len(matrix[0])-1:
        if matrix[rowNum][colNum]==cost:
            return 1
        else:
            return 0
    op1 = reachLastCell(matrix, rowNum+1, colNum, cost-matrix[rowNum][colNum])
    op2 = reachLastCell(matrix, rowNum, colNum+1, cost-matrix[rowNum][colNum])
    return op1+op2


TwoDList = [[4,7,1,6],
           [5,7,3,9],
           [3,2,1,2],
           [7,1,6,3]
           ]

print(reachLastCell(TwoDList, 0,0, 25))
    
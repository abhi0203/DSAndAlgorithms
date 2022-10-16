'''
The problem statement is ,

Given number N, find ways to express N as sum of 1,3,4

So here imagine we are given a number 5 it can be represented as 
1,1,1,1,1  --> 1,1,3 --> 1,4 --> 3,1,1 --> 4,1

so a total of 5 ways this can be represented.
now how do we divide this into smaller problems. 

- We can use only the combinations of the given 3 numbers. 
- Basically how we can divide the work is, we can as long as the sum is less than the number we want to achieeve, we should increase the count and then subtract the number from the target number. 
- so for example, we have to make 5 using 1,3 and 4.
- There will be atleast 3 ways to make it. 
- In the first one, add 1 and then recursively call for 5-1 which is 4. 
- We do the same for remaining. 
- In the next stack of the recursive calle, we use the subtracted number
- This recursive call goes on till we hit < 0 in which case, we should return 0 as this is not the right way to form the number
- And if we hit a case where we hit the mainNum as exact 0, then in that case, 
- Finally we return the sum of the numbers
'''

def numberFactor(mainNum, num1, num2,num3):
    # Write the base case, where in if the minNum is <=0 return 0
    if mainNum<0:
        return 0
    if mainNum==0:
        return 1
    op1= numberFactor(mainNum-num1, num1, num2, num3)
    op2= numberFactor(mainNum-num2, num1, num2, num3)
    op3= numberFactor(mainNum-num3, num1, num2, num3)

    return op1+op2+op3

print(numberFactor(5,1,3,4))
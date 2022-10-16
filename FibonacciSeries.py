'''
In this method, we are trying to write a divide and condquor algorithm for Fibonacci series.
In tthe divide and conquor algorithm, we basically divide the larger problem into smaller subproblems and then solve them. Finally combine the solutions to get the answer.
If we have to caluclate Fibonacci of a number, the it is the sum of previous 2 numbers.
For example, Fib 0 is 0 and Fib of 1 is 1.
Fib 2 is Fib(0) + Fib (1) = 0+1 = 1
Fib of 3 is Fib(2) + fib(1)= 1 + 1= 2
Fib(4) if Fib(3)+ Fib(2)= Fib(2) + Fib(1) + Fib(1)+ Fib(0) = 1 + 1 + 1 + 0 = 3
So the fibonacci series is defined as 0,1,1,2,3,5,8,13..... and so on.

So by similar logic, we are calculating the Fib(10) with Fib(9)+ Fib(8) and so on......
So we divided the work into smaller pieces of getting the number Fib of 9 and 8. 
We divide the problem until its base case and then return the results.
'''

def fibonacci(num):
    #Below are the base cases
    if num==0:
        return 0
    if num== 1:
        return 1 
    return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(200))
# Outcome should be 5
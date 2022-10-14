'''
In this case, we are given a list of coin denominations and a number that we want to form.
It is assumed that the number can be formed with those denominations. 
We need to form the number with minimum number of coins.

- Here also, we can use Greedy algorithm. In this case, we can first sort the denominations if they are not already sortted.
- The sorting can happen in the reverse order.
- Once the sortig happens, we then start with the largest number.
- If the number is less than the number we need to make, we subtract that number from the finalNum.
- We then again check if the largest number is less than finalNum.
- If the number is greater than the finalNum, we then move on to next number and so one.
- Since it is mentioned that denomination will always happen, we can break when we reach the final number. 

coins = [1,2,5,20,50,100]
coinChange(201, coins)


'''


from audioop import reverse


def coinChange(finalNum, coins):
    coins.sort(reverse= True)
    # Start with the last number in the coins in the loop.
    # Since we can use unlimited number of denominations, we should run the loop infinitely.
    i= 0
    while True:
        if coins[i]<= finalNum:
            print(coins[i])
            finalNum= finalNum- coins[i]
        else:
            i+=1
        if finalNum==0:
            break
    
coins = [1,2,5,20,50,100]
coinChange(201, coins)
        



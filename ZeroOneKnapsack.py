"""
Problem Statement:
- Given the weights and profits of the specific items
- Find the maimum profit within capacity C
- Items cannnot be broken like the fractiosnal knapsack problem. 

As we saw in the fractioanl knapsack, since we can create fractions, we can use the greedy algorithm there where we fix something that gives the highest value and then move from there.
It is the fractions that allows us to do so. But here in this case, since we cannot have fractions, we have to be using divide and conquor algorithm as we have try with "potentially" all the combinations of items and check which one gives us the maximum benefit. 

How do we divide the work?
- We can use the same techniques that we used for the robber problem where in we moved from one itema and second item and so on. 
- Here we have a constraint of maximum weight so as long as we are not crossing it, it should be good. 

So we have to do is try with all the combinations to see which one can maximize the profit.

- We can divide the work based on current element and the next element.
- If the current size is less that the size of the sack, we can add it in the sack and use its value. 
    - We can then call the function recursively with remaining capacity and remaining items.
- Similary, to add flavour and not treat it like the list, we can skip the current item and just call the function recursivelyy on the next item. 
- Finally we return the max of cost at that level without passing the limit.

What are the base conidtions?
- Since we plan to add the current value to the list, we want to make sure that it is not greater than the capacity. Else return 0
- Also, while the capacity is sent, if it is ==0 then we just send 0 back.
- We might have to check the same for second element. 
- To represent the elements, we can create an item class.

"""

from pydoc import cli


class Item:
    def __init__(self, weight, value):
        self.weight= weight
        self.value= value

def zoKnapSack(cList, idx, capacity):
    #If we are reching the capacity and nothing left, we simply return
    if capacity== 0:
        return 0
    #If we have reached the end of the array, we simply leave and return
    if idx>=len(cList):
        return 0
    #If the current idx weight capacity is greater (since we cannot use fractiosn) we return
    if cList[idx].weight> capacity:
        return 0
    else:
        option1 = cList[idx].value + zoKnapSack(cList, idx+1, capacity- cList[idx].weight)
        option2 = zoKnapSack(cList, idx+1, capacity)
        return max(option1, option2)

mango= Item(3,31)
apple= Item(1,26)
orange= Item(2,17)
banana= Item(5,72)

cList= [mango, apple, orange, banana]
print(zoKnapSack(cList, 0, 5))


    
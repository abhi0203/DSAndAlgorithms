'''
In this case, we are given capacity and value per item. We are then given a sack which has final capacity that we can include. What we need to do is, add the items in such a way that we maximize the value in that sack.
The key here is, we can use fractional parts in this case to maximize the value. 

- What we need to do is, we need to calculate the value per unit capacity and then sort it in the reverse order.
- Once we are done with that we need to start with the one that gives highest value per unit capacity item and then keep on adding that item to sack until we finish the capacity of the item or we reach the capacity of the sack.

'''

class Item:
    def __init__(self, capacity, value):
        self.capacity= capacity
        self.value= value
        self.ratio= value/ capacity

def knapsackMethod(cList, capacity):
    #First sort the cList using the value in the reverse order
    cList.sort(key=lambda x:x.ratio, reverse= True)
    # now start a loop where in start with the current capacity and compare it with capacity.
    # we then move the through list one by one and start adding the value 
    currentCapacity= 0
    totalValue= 0
    for item in cList:
        itemCapacity= 0
        while currentCapacity < capacity and itemCapacity< item.capacity:
            currentCapacity+= 1
            totalValue+= item.ratio
            itemCapacity+= 1
        if currentCapacity==capacity:
            break
    print(totalValue)
    return


item1 = Item(20,100)
item2 = Item(30,120)
item3 = Item(10,60)
cList = [item1, item2, item3]

knapsackMethod(cList, 50)
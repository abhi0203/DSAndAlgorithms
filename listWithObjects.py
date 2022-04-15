class Node:
    def __init__(self, data):
        self.data= data


myList= []

for i in range(10):
    myList.append(Node(i))


print(myList)
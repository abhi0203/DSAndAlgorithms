def productOfArray(arr):
    if arr==[]:
        return None
    else:
        return arr[0]* productOfArray(arr[1:])


print(productOfArray([-1,2,3,-12,21]))

# Empty array
# 
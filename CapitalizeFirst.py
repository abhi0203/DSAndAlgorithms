def capitalizeFirst(arr):
    if arr==[]:
        return []
    else:
        arr[0]= arr[0][0].upper()+arr[0][1:]
        print("First One",arr)
        arr.append(capitalizeFirst(arr[1:]))
        print("Second Item ",arr)
        return arr
    # Dont know about th eedge cases
    #- What if there are numbers as strings
    #- What if already capital
    #- Can there be array within array?

print(capitalizeFirst(['car','taco','banana']))
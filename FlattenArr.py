def flatten(arr):
    final_arr=[]
    if arr==[]:
        return None
    for i in arr:
        if isinstance(i, list):
            final_arr .extend(flatten(i))
        else:
            final_arr.append(i)
    return final_arr
            

print(flatten([1,2,3,[4,5],6,7,8,[9,10,11]]))
'''
Given and input array that containes any numbers.
Return an array that has product of that array except self.

Cases about zero as we have to avoid those arrays

'''

def ProductExceptSelf(inputArray):
    if inputArray==[]:
        return []
    product= 1
    zeroCount= 0
    outputArray=[]
    for i in inputArray:
        if i==0:
            zeroCount+=1
            if zeroCount>1:
                return [0]*len(inputArray)
        product= product*i
    
    if product==0:
        product=1
        for i in range(len(inputArray)):
            if inputArray[i]==0:
                zeroLocation=i
                continue
            else:
                product= product* inputArray[i]
        outputArray= [0] * len(inputArray)
        outputArray[zeroLocation]= product
        return outputArray
    else:
        for i in inputArray:
            outputArray.append((product/i))
    
    return outputArray

    

print(ProductExceptSelf([1,2,3]))
print(ProductExceptSelf([-1,2,3]))
print(ProductExceptSelf([1,2,0]))
print(ProductExceptSelf([1,0,0]))

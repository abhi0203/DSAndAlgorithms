'''
Problem Statement is,
- S1 and S2 are the strings given to us
- Convert S2 to s1 using delete, insert and replace operations. 
- Find the minimum count of edit operations. 

Again this is divide and conquor type problem as we have see all the possible counts and then find the minimum one. 

So we are given 2 strings and we have to calculate minimum operations we need to make s2 = s1.
Can this makes difference if S2 is made into s1 or S1 is made into s2? (Seems the number of operations remains the same)
Basically we are told that we are given 3 operations and that is what is gives us the line to divide and conquor.

What we have to do is, start with the current index of the list. 
- If the alphabates are the same, then there is no problem and we move on to the next index.
- If they are not the same, that is when we have to perform one of insert, delete or replace operation.
- If we perform insert operation, then we should move the index of the S1 to the next elemet and compare it with existing element of the second string.
- If we perform the delete operations (which is expected on second string) then we move the index of the second string to the next item and compare it with first strinf.
- if we we performs replace operation, then we have to move both the indices. 

At the end, we calculate the minimum of the 3 operations that we had to perform and send them up the recursive call.

Finally there are some base conditions.
-if s1 is smaller or we reach the end of s1 before s2, then whatever are the elements left in s2, that many operations are needed.
- if s2 is smaller or we reach to the end of s2, then whatever elements left in the s1 will the number of operations.

'''


def convertString(s1, s2, idx1, idx2):
    if idx1 >= len(s1):
        # This means we are at the end of s1, so whatever the number of elements in s2, are the number of operations we need to performd
        return len(s2)- idx2
    if idx2>= len(s2):
        # THis means, we are at the end of s2 and whatever are the number of operations in s1, we need to perform them
        return len(s1)-idx1
    # Case where they both are the same
    if s1[idx1]== s2[idx2]:
        # Here we simply recurse over the next elements.
        return convertString(s1, s2, idx1+1, idx2+2)
    else:
        # Now we know for sure that we have to do one of insert, delete or replace operation.
        # The one we add represent that we considered that operation and now want to move on to the next operations. 
        op1= 1 + convertString(s1,s2, idx1+1 , idx2) # insert
        op2= 1 + convertString(s1, s2, idx1, idx2+1) # delete
        op3= 1 + convertString(s1, s2, idx1+1, idx2+1) # replace
        return min(op1, op2, op3)


print(convertString("table", "", 0, 0))
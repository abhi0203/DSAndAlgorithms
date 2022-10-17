"""
Problem statement
- S is the given string.
- We need to find the longest palindromic sub sequesce from the string.
- Subsequence is a sequence that can be deloivered from another sequence, by deleting some elements but without changing the order of the string.
- Palindrome is a string that is same if read backword and forward.
- The number that should be returned is the number of elements in the string.

Eg: Abhiram it is 3 as the palindromic string is "aba" or "aha" etc.

Since we need to return the count of the length of the longest substring, we can use divide and conquer. 
How do we divide the problem?
- If I just have to find if a string is a palindrome, then all I need is left and right pointer, and then compare. 
- How do we divide the work is in actual substring finding. 
- So if the left and right pointers are are same, then we can add 1 and move both pointers in the respective directions and call the function recursively.
- If the pointers do not match, we can use the divide and conquer in the sense that in one option, we increase the first pointer forward and in the next case we move the last pointer one place less.
- The call should retun the length that can be added upwords.
- So we return the max of the the 2. 

What are the base cases.
- One of the pointer has reached end i.e. start>= len(array) or end <= -1
- end is < start
- If they point to the same element, we should add 1

"""

def lpSubSequence(str1, start, end):
    if start>=len(str1) or end<=-1:
        return 0
    if start==end:
        return 1
    if start> end:
        return 0
    if str1[start]== str1[end]:
        return 2+ lpSubSequence(str1, start+1, end-1)
    else:
        op1= lpSubSequence(str1, start+1, end)
        op2= lpSubSequence(str1, start, end-1)
        return max(op1,op2)

s1= "niia"
print(lpSubSequence(s1, 0, len(s1)-1))

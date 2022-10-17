"""
Problem Statement:
- S1 and S2 are 2 string.
- Find the length of the longest subsequence which is common in both strings.
- Subsequence: It is derived from another sequence by deleting one or more items, without changing their order. 

So we have to find the common elements from both of them. 
So on a high level, we compare the items one by one. if they match then we add to the number.
If they dont match, we once increase the number of first string andf keep second string at same 
Or we move other string further and keep it same.

We should add it to the count only if the string matches else we are not adding it. 
What are the base conditions?
- I think us reaching the end of one of the string should be enough to return
- Also, while returnin, we should consider the maximum of the two elements.

"""


def lcSequence(s1, s2, idx1, idx2):
    if idx1>= len(s1) or idx2>= len(s2):
        return 0
    if s1[idx1]==s2[idx2]:
        return 1+ lcSequence(s1, s2, idx1+1, idx2+1)
    else:
        count1= lcSequence(s1, s2, idx1+1, idx2)
        count2= lcSequence(s1, s2, idx1, idx2+1)
        return max(count1, count2)

print(lcSequence("abhiram", "neha", 0 ,0))
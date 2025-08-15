'''
Name: 392. Is Subsequence
Link: https://leetcode.com/problems/is-subsequence/description/
'''

# Approach 1: Two pointers
def isSubsequence(s, t):
    sp = tp = 0

    while sp < len(s) and tp < len(t):
        if s[sp] == t[tp]:
            sp += 1
        tp += 1
    
    return sp == len(s)

# Test case:
s = "axc"
t = "ahbgdc"
print(isSubsequence(s, t))

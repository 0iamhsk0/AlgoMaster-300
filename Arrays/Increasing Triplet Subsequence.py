'''
Name: 334. Increasing Triplet Subsequence
link: https://leetcode.com/problems/increasing-triplet-subsequence/
'''

# Approach 1:
def increasingTriplet(nums):
    first = second = float('inf') 
    for n in nums: 
        if n <= first: 
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False

# Test case
nums = [2,1,5,0,4,6]
print(increasingTriplet(nums)) #True
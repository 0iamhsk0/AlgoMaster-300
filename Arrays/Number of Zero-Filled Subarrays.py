'''
Name: 2348. Number of Zero-Filled Subarrays
Link: https://leetcode.com/problems/number-of-zero-filled-subarrays/description/
'''

# Approach 1: Increment zero when having 0 contig array, reset it when contgious fails
def zeroFilledSubarray(nums):
    zero_count = 0
    zero_seq_count = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            zero_seq_count += 1
            zero_count += zero_seq_count
        else:
            zero_seq_count = 0
    
    return zero_count

# Test case:
nums = [1,0,0,4,3,0,0,0,8,0]
print(zeroFilledSubarray(nums)) # 10
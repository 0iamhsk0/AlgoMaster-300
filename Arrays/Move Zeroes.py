'''
Name: 283. Move Zeroes
Link: https://leetcode.com/problems/move-zeroes/description/
'''

# Approach 1: Brute force
def moveZeroes1(nums):
    n = len(nums)
    if n < 1:
        return nums
    for i in range(n):
        if nums[i] == 0:
            nums.remove(0)
            nums.insert(n-1, 0)
    return nums

# Approach 2: Two pointers
def moveZeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
    return nums

# Test case:
nums = [0,1,0,3,12]
moveZeroes(nums) # [1,3,12,0,0]
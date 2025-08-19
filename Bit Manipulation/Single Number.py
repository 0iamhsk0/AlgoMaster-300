'''
Name: 136. Single Number
Link: https://leetcode.com/problems/single-number/description/
'''

# Approach 1: Using XOR
def singleNumber(nums):
    n = len(nums)
    res = 0
    #base case:
    if n == 1:
        return nums[0]
    for num in nums:
        res ^= num
    return res

# Test Case:
nums = [4,1,2,1,2]
print(singleNumber(nums)) # 4

# Approach Many: Hashmap, lists, counters etc etc but space will be O(N) which violates the question
def singleNumber2(nums):
    n = len(nums)
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    for num, freq in counter.items():
        if freq == 1:
            return num
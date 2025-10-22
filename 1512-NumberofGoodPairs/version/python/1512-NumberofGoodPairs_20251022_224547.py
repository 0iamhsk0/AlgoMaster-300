# Last updated: 10/22/2025, 10:45:47 PM
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        hash_map = dict()
        for num in nums:
            if num in hash_map:
                cnt += hash_map[num]
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        
        return cnt


        
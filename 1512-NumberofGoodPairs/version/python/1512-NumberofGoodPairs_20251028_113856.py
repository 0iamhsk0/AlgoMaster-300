# Last updated: 10/28/2025, 11:38:56 AM
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_map = {}
        cnt = 0
        for i in nums:
            if i in hash_map:
                cnt += hash_map[i]
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        return cnt
        

        
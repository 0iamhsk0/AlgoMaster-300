# Last updated: 12/1/2025, 11:36:58 PM
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        #brute:
4        # for i in range(len(nums)):
5        #     for j in range(len(nums)):
6        #         if nums[i] == nums[j] or abs(i-j) <= k:
7        #             return True
8        #         else:
9        #             return False
10
11        #using sets or dict:
12        # seen = set()
13        # for i, num in enumerate(nums):
14        #     if num in seen:
15        #         return True
16        #     else:
17        #         seen.add(num)
18        #     if len(seen) > k:
19        #         seen.remove(nums[i-k]) #which will be the first index
20        # return False
21
22        num_index={}
23        for index,num in enumerate(nums):
24            if num in num_index and abs(index-num_index[num])<=k:
25                return True
26            else:
27                num_index[num]=index        
28        return False
29    
30
31        
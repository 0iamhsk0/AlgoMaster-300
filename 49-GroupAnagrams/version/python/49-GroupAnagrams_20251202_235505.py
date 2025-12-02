# Last updated: 12/2/2025, 11:55:05 PM
1# Method - 1: Sorting, popping and storing
2
3class Solution:
4    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
5        ans = defaultdict(list)
6
7        for s in strs:
8            key = "".join(sorted(s))
9            ans[key].append(s)
10        
11        return list(ans.values())
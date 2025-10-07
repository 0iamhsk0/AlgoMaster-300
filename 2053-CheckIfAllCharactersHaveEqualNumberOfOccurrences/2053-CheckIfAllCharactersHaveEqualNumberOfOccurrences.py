# Last updated: 10/7/2025, 6:51:51 PM
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for i in s: 
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        all_vals = d.values()
        return len(set(all_vals)) == 1

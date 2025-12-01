# Last updated: 12/1/2025, 11:16:15 PM
1class Solution:
2    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
3        if len(ransomNote) > len(magazine):
4            return False
5            
6        for c in set(ransomNote):
7            if magazine.count(c) < ransomNote.count(c):
8                return False
9
10        return True
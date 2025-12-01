# Last updated: 12/1/2025, 11:17:40 PM
1# Method - 1: Counter
2# from collections import Counter
3
4# class Solution:
5#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
6#         return not (Counter(ransomNote) - Counter(magazine))
7
8# Method 2: Hashmap
9class Solution:
10    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
11        mag_hash = {}
12
13        for letter in magazine:
14            mag_hash[letter] = 1 + mag_hash.get(letter, 0)
15        
16        for letter in ransomNote:
17            if letter not in mag_hash or mag_hash[letter] <= 0:
18                return False
19            mag_hash[letter] -= 1
20
21        return True
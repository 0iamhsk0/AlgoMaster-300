# Last updated: 12/13/2025, 9:29:17 PM
1class Solution:
2    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
3    
4        def is_sub(word):
5            index=-1
6            for ch in word:
7                index=s.find(ch,index+1)
8                if index==-1:
9                    return False
10            return True
11        
12        c=0
13        for word in words:
14            if is_sub(word):
15                c+=1
16        
17        return c
18	
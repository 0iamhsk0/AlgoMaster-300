# Last updated: 10/8/2025, 11:11:04 PM
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i == '*':
                stack.pop()
            else:
                stack.append(i)
        
        return ''.join(stack)

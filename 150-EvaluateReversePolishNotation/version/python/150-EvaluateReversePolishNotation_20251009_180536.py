# Last updated: 10/9/2025, 6:05:36 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(token))

        return stack[-1]


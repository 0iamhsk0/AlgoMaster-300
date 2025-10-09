# Last updated: 10/9/2025, 7:07:59 PM
class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        cur = prev = res = 0
        cur_operation = "+"

        while i < len(s):
            cur_char = s[i]
            if cur_char.isdigit():
                cur = 0
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1

                if cur_operation == "+":
                    res += cur
                    prev = cur
                elif cur_operation == "-":
                    res -= cur
                    prev = -cur
                elif cur_operation == "*":
                    res -= prev
                    res += prev * cur
                    prev = prev * cur
                else:
                    res -= prev
                    res += int(prev / cur)
                    prev = int(prev / cur)

                cur = 0
            if i < len(s) and s[i] in "+-*/":
                cur_operation = s[i]
            i += 1
        return res

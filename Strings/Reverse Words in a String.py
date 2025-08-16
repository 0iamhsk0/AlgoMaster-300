'''
Name: 151. Reverse Words in a String
Link: https://leetcode.com/problems/reverse-words-in-a-string/description/
'''

# Approach 1:
def reverseWords(s: str) -> str:
    stripped_string = s.split()
    ans = []

    for i in range(len(stripped_string) - 1, -1, -1):
        ans.append(stripped_string[i])
        if i != 0:
            ans.append(" ")

    return "".join(ans) 

# Test case:
s = "  hello world  "
print(reverseWords(s)) # world hello
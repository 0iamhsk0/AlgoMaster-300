'''
Name: 125. Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/description/
'''

# Approach 1: Using in build methods
def isPalindrome(s):
    filtered_string = ''.join(char.lower() for char in s if char.isalnum())
    
    n = len(filtered_string)
    for i in range(n // 2):
        if filtered_string[i] != filtered_string[n - i - 1]:
            return False
    return True

# Approach 2: Using Regex methods
import re
def isPalindrome(s):
    new_str = re.sub('[^a-zA-Z0-9]','',s).lower()
    rev_str = new_str[::-1]
    if new_str == rev_str:
        return True
    return False

# Test case:
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s)) #True #"amanaplanacanalpanama"
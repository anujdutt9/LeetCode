# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

# Input: "A man, a plan, a canal: Panama"
# Output: true

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove all spaces, special characters from string using .isalnum()
        strng = ''.join(e for e in s if e.isalnum()).lower()
        # Check if string is equal to string reversed
        if (strng == strng[::-1]):
            return True
        return False
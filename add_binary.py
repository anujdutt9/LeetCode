# Add Binary
# https://leetcode.com/problems/add-binary/

# Given two binary strings, return their sum (also a binary string).
# Input: a = "11", b = "1"
# Output: "100"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Add two numbers as Int with base 2.
        # Convert them to binary and then a string.
        return str(bin(int(a, 2) + int(b, 2))).split('b')[1]
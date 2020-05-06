#  Longest Substring Without Repeating Characters
# https://leetcode.com/explore/interview/card/apple/344/array-and-strings/2009/

# Using Sliding Window Approach
def lengthOfLongestSubstring(s: str) -> int:
    # Check if Length of String in Zero
    if len(s) is None:
        return 0
    # Starting Index
    start = 0
    # Length of Subsctring
    max_len = 0
    # Dictionary to hold characters
    d = {}
    
    for i in range(len(s)):
        if s[i] in d and start <= d[s[i]]:
          # Increment Starting Index by 1
          start = d[s[i]] + 1
        else:
          # Get Length of non repeatable characters
          max_len = max(max_len, i - start + 1)
        # Add character to Dictionary 
        d[s[i]] = i
    return max_len

# Test Cases
st = "abcabcbb"
print(lengthOfLongestSubstring(st))
assert lengthOfLongestSubstring(st) == 3

st = "ABDEFGABEF"
print(lengthOfLongestSubstring(st))
assert lengthOfLongestSubstring(st) == 6

st = "GEEKSFORGEEKS"
print(lengthOfLongestSubstring(st))
assert lengthOfLongestSubstring(st) == 7

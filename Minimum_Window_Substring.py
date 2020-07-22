# Minimum Window Substring

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''
        
        d = Counter(t)
        required = len(d)
        left, right = 0, 0
        
        ans = float("inf"), None, None
        window_count = {}
        formed = 0
        
        while right < len(s):
            # Move Right Pointer Forward
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            if char in d and window_count[char] == d[char]:
                formed += 1
            
            # Move Left Pointer
            while left <= right and formed == required:
                char = s[left]
                
                # Save the Smallest Window
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                window_count[char] -= 1
                
                if char in d and window_count[char] < d[char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return '' if ans[0] == float('inf') else s[ans[1]: ans[2] + 1]

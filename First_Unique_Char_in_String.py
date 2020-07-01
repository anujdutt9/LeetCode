# First unique character in a string

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] +=1

        for key,val in d.items():
            if val == 1:
                return s.index(key)
        return -1

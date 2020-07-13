# Word Break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False
        
        n = len(s)
        ans = [False for u in range(n+1)]
        ans[0] = True
        
        for i in range(n):
            if ans[i]:
                for word in wordDict:
                    l = len(word)
                    if i + l <= n and s[i: i+l] == word:
                        ans[i + l] = True
        return ans[-1]

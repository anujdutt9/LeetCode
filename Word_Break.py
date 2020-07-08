# Word Break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == '':
            return True
        else:
            n = len(s)
            return any([(s[:i] in wordDict) and self.wordBreak(s[i:], wordDict) for i in range(1, n + 1)])

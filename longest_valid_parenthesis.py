# Longest Valid Parenthesis

def longestValidParenthesis(s):
  max_len = 0
  stack = []
  stack.append(-1)

  for i in range(len(s)):
    if s[i] == '(':
      stack.append(i)
    else:
      stack.pop()

      if len(stack) <= 0:
        stack.append(i)
      else:
        max_len = max(max_len, i - stack[-1])
  
  return max_len

s = '((()'
print(longestValidParenthesis(s))

s1 = ')()())'
print(longestValidParenthesis(s1))

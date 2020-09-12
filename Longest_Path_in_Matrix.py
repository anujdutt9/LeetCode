# Find the longest path in a Matrix with given constraints

def findLongestOverall(matrix):
  rows = len(matrix)
  cols = len(matrix[0])

  dp = [[-1 for j in range(cols)] for i in range(rows)]

  result = 1
  ans = []

  for i in range(rows):
    for j in range(cols):
      if dp[i][j] == -1:
        findLongestPath(matrix, i, j, dp)
      result = max(result, dp[i][j])
  return result


def findLongestPath(matrix, i, j, dp):
  if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
    return 0
  
  if dp[i][j] != -1:
    return dp[i][j]
  
  up, down, left, right = -1, -1, -1, -1
  
  if i > 0 and (matrix[i][j] + 1 == matrix[i-1][j]):
    down = 1 + findLongestPath(matrix, i-1, j, dp)
  
  if i < len(matrix) - 1 and (matrix[i][j] + 1 == matrix[i+1][j]):
    up = 1 + findLongestPath(matrix, i+1, j, dp)
  
  if j > 0 and (matrix[i][j] + 1 == matrix[i][j-1]):
    right = 1 + findLongestPath(matrix, i, j-1, dp)
  
  if j < len(matrix[0]) - 1 and (matrix[i][j] + 1 == matrix[i][j+1]):
    left = 1 + findLongestPath(matrix, i, j+1, dp)
  
  dp[i][j] = max(up, max(down, max(left, max(right, 1))))
  return dp[i][j]

matrix = [[1, 2, 9],
        [5, 3, 8],
        [4, 6, 7]]
        
print(findLongestOverall(matrix))

# Jumping Numbers

def jumpingNumbers(num):
  if not num:
    return
  
  for i in range(10):
    if i <= num:
      bfs(num, i)

# BFS
def bfs(num, i):
  queue = []
  queue.append(i)

  while queue:
    tmp = queue.pop()

    if tmp <= num:
      print(str(tmp) + '')

      last_digit = tmp % 10

      # we can only go to 1 from 0
      if last_digit == 0:
        queue.append((tmp * 10) + (last_digit + 1))
      # we can only go to 8 from 9
      elif last_digit == 9:
        queue.append((tmp * 10) + (last_digit - 1))
      # for all other digits, push in prev and next digit
      # ex. if last_digit = 3, push 32 (3 * 10 + 3 - 1) and 
      # 34 (3 * 10 + 3 + 1) to queue
      else:
        queue.append((tmp * 10) + (last_digit - 1))
        queue.append((tmp * 10) + (last_digit + 1))

# Test
jumpingNumbers(40)
jumpingNumbers(10)

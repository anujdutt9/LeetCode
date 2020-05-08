# 3 Sum Closest
# 

def threeSumClosest(nums: [int], target: int) -> int:
  # Sort the Array
  nums.sort()
  
  # Reference Sum
  res = sum(nums[:3])

  for i in range(len(nums) - 2):
    # Define Left and Right Pointer
    left = i + 1
    right = len(nums) - 1

    while left < right:
      total = nums[i] + nums[left] + nums[right]
      
      # Compare the absolute Values
      if abs(total - target) < abs(res - target):
        res = total

      if total > target:
        right -= 1
      elif total < target:
        left += 1
  
  # Return Result
  return res

# Test Cases
n = [-1,2,1,-4]
t = 1 
print(threeSumClosest(n, t))
assert threeSumClosest(n, t) == 2

n = [0,0,0]
t = 1 
print(threeSumClosest(n, t))
assert threeSumClosest(n, t) == 0

n = [1,1,1,0]
t = -100
print(threeSumClosest(n, t))
assert threeSumClosest(n, t) == 2

n = [0,2,1,-3]
t = 1
print(threeSumClosest(n, t))
assert threeSumClosest(n, t) == 0

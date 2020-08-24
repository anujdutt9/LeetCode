# Find Index of Subarray with Given Sum

def subarraySum(nums, target):
  n = len(nums)
  i = 0
  start = 0
  curr_sum = 0

  while i <= n:
    
    while curr_sum > target and start < i - 1:
      curr_sum = curr_sum - nums[start]
      start += 1

    if curr_sum == target:
      print("%d %d"%(start, i-1))
      return 1
    
    if i < n:
      curr_sum += nums[i]
    
    i += 1
  
  print("No subarray found")
  return

# Test
nums = [1,2,3,5,7]
target = 10
subarraySum(nums, target)

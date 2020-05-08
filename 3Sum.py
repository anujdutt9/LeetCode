# 3Sum
# https://leetcode.com/explore/interview/card/apple/344/array-and-strings/2012/

def threeSum(nums: [int]):
  # Array to contain results
  result = []
  
  # Sort the Input Array
  nums = sorted(nums)
  
  for i in range(len(nums) - 2):
    # Check for same consecutive initial values
    if i > 0 and nums[i] == nums[i-1]:
      continue
    
    # Left Pointer
    left = i + 1
    
    # Right Pointer
    right = len(nums)-1
    
    # While left < right
    while left < right:
      # Get the Sum of three numbers
      s = nums[i] + nums[left] + nums[right]
      
      # If the sum is greater than 0, decrement the right pointer
      # as our array is sorted and decrementing this will reduce the +ve values.
      if s > 0:
        right -= 1
        
      # If the sum is less than 0, increment the left pointer
      # as our array is sorted and incrementing this will reduce the -ve values.
      elif s < 0:
        left += 1
      
      # Else our sum was equal to zero, append the values to our array
      else:
        result.append([nums[i], nums[left], nums[right]])
        
        # Check for left and right pointers for repeatable numbers
        while left < right and nums[left] == nums[left + 1]:
          left += 1
        
        while left < right and nums[right] == nums[right - 1]:
          right -= 1
        
        # Increment Left pointer
        left += 1
        # Decrement Right Pointer
        right -= 1
  
  # Return the result
  return result


# Test Cases
n = [-1, 0, 1, 2, -1, -4]
print(threeSum(n))
assert threeSum(n) == [[-1, -1, 2], [-1, 0, 1]]

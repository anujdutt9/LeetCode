# Roman to Integer
# https://leetcode.com/explore/interview/card/apple/344/array-and-strings/3107/

def romanToInt(s: str) -> int:
  # Dictionary with Roman to Integer Mapping
  d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

  # Variables to store Values
  result = 0
  previous = 0
  current = 0

  for i in range(len(s)):
    # Current Int value
    current = d[s[i]]

    # If the Current Int value > Previous Int value then,
    # result = (result + current - 2 * previous)
    if current > previous:
      result += current - 2 * previous
    else:
      # otherwise, just add the current value to result
      result += current
    
    # Set previous value to current value
    previous = current
  
  # Return Result
  return result


# Test Cases
print(romanToInt("I"))
assert romanToInt("I") == 1

print(romanToInt("MMXX"))
assert romanToInt("MMXX") == 2020

print(romanToInt("MDCCLXXVI"))
assert romanToInt("MDCCLXXVI") == 1776

print(romanToInt("XXIII"))
assert romanToInt("XXIII") == 23

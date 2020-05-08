# Integer to Roman
# https://leetcode.com/explore/interview/card/apple/344/array-and-strings/3106/

def intToRoman(num: int) -> str:
  # Array representing the Roman Representation of Numbers in Descending Order
  roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"] 
  
  # Array representing the integer values for the corresponding Roman Numerals
  ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  
  # String for the Final Result
  result = ''
  
  # Check for range of Input Numbers
  if num > 3999 or num < 1:
    return

  # Go through all the numbers in the Ints array
  for i in range(len(ints)):
    # While the Input Number - current value in Ints is >= 0,
    # add the corresponding Roman Numeral to the result
    # and subtract the corresponding int value from the number
    while(num - ints[i] >= 0):
      result += roman[i]
      num -= ints[i]
  
  # Return final result
  return result


# Test Cases
print(intToRoman(49))
assert intToRoman(49) == "XLIX"

print(intToRoman(2020))
assert intToRoman(2020) == "MMXX"

print(intToRoman(23))
assert intToRoman(23) == "XXIII"

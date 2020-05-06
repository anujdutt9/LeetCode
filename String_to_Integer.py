# String to Integer (atoi)
# https://leetcode.com/explore/interview/card/apple/344/array-and-strings/2010/

def myAtoi(s: str) -> int:
  # If string is empty
  if len(s) == 0:
    return 0
  
  # Variable to store result
  result = 0

  # If string has values but with whitespaces
  s = s.strip()

  # Test for Edge Case i.e. " "
  if not s:
    return 0

  # Check for -ve/+ve signs
  negative = False
  if s[0] == '-':
    negative = True
  elif s[0] == '+':
    negative = False
  # If the first character is not numeric i.e. a string or something else
  elif not s[0].isnumeric():
    return 0
  else:
    # Get the original character as int
    # ex: ord("4") - ord("0") = 52 - 48 = 4
    result = ord(s[0]) - ord("0")
  
  # Since character at index "0" has been taken care of, we start from the character at index "1"
  for i in range(1, len(s)):
    # Check if charcater is numeric
    if s[i].isnumeric():
      # Compute Result
      result = result*10 + (ord(s[i]) - ord("0"))

      # Check if result is within the -ve/+ve Int range
      if not negative and result > 2**31 - 1:
        return 2**31 -1
      elif negative and result >= 2**31:
        return -2**31
    else:
      # character is not numeric, go to next one
      break
  
  # Handle the -ve/+ve signs for final result
  if negative:
    return -result
  else:
    return result


# Test Cases
st = ""
print(myAtoi(st))
assert myAtoi(st) == 0

st = " "
print(myAtoi(st))
assert myAtoi(st) == 0

st = "words and 987"
print(myAtoi(st))
assert myAtoi(st) == 0

st = "19"
print(myAtoi(st))
assert myAtoi(st) == 19

st = "   -42"
print(myAtoi(st))
assert myAtoi(st) == -42

st = "  101  "
print(myAtoi(st))
assert myAtoi(st) == 101

st = "+239"
print(myAtoi(st))
assert myAtoi(st) == 239

# > Int +ve range
st = "2147483650"
print(myAtoi(st))
assert myAtoi(st) == 2147483647

# < Int -ve range
st = "-2147483650"
print(myAtoi(st))
assert myAtoi(st) == -2147483648

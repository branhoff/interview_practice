"""
## Validating Near-Palindrome Strings

Write a function that takes a string as input and checks whether it can be a valid palindrome by removing at most one character from it.

**Constraints**
 - $1 \leq$ `string.length` $\leq10^3$
- The string only consists of English letters
"""

def is_valid_near_palindrome(string):
  left = 0
  right = len(string) - 1
  num_removed = 0

  while left < right:
    if string[left] == string[right]:
      left += 1
      right -= 1
    elif string[left+1] == string[right] and num_removed == 0:
      left += 1
      num_removed += 1
    elif string[left] == string[right-1] and num_removed == 0:
      right -= 1
      num_removed += 1
    else:
      return False

  return True


def main():
  inputs = [
    "ababbaba",
    "ababdcaba",
    "racecar",
    "madame",
    "emadam",
    "dead",
    "tebbem",
    "eeccccbebaeeabebccceea"
  ]

  expected_output = [
    True,
    False,
    True,
    True,
    True,
    True,
    False,
    False
  ]

  for i, string in enumerate(inputs):
    actual_result = is_valid_near_palindrome(string)
    expected_result = expected_output[i]

    print(f"{i + 1}.\tInput String:\t\t{string}")
    print(f"\tIs near palindrome:\t{actual_result}")

    # Assertion to check if the actual result matches the expected result
    if actual_result != expected_result:
      print(f"Test failed for input: {string}. Expected: {expected_result}, got: {actual_result}")
    else:
      print(f"Test passed")

    print("-" * 100)

if __name__ == '__main__':
  main()
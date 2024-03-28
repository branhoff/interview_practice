"""
Write an algorithm to determine if a number $n$ is a happy number.

We use the following process to check if a given number is a happy number:

Starting with the given number $n$, replace the number with the sum of the squares of its digits.
Repeat the process until:
- The number equals $1$, which will depict that the given number $n$ is a happy number.
- The number enters a cycle, which will depict that the given number $n$ is not a happy number.

Return `True` if $n$ is a happy number, and `False` if not.

**Constraints**
$1 \leq n \leq 2^{31} − 1$
"""

def sum_of_squared_digits(n):
  digit_sum = 0
  while n > 0:
    digit_sum += (n % 10) ** 2
    n //= 10
  return digit_sum

def is_happy_number(n):
  slow_pointer = n
  fast_pointer = sum_of_squared_digits(n)

  while slow_pointer != fast_pointer:
    slow_pointer = sum_of_squared_digits(slow_pointer)
    fast_pointer = sum_of_squared_digits(sum_of_squared_digits(fast_pointer))

    if fast_pointer == 1:
      return True

  return False

def main():
  inputs = [
    4,
    23,
    163,
    2147483646,
    1,
    19,
    8,
    7
  ]

  expected_results = [
    False,
    True,
    False,
    False,
    False,
    True,
    False,
    True
  ]

  for i, n in enumerate(inputs):
    actual_result = is_happy_number(n)
    expected_result = expected_results[i]

    print(f"{i + 1}.\tInupt n:\t\t{n}")
    print(f"\tResult:\t{actual_result}")

    # Assertion to check if the actual result matches the expected result
    if actual_result != expected_result:
      f"Test failed for input: {n}. Expected: {expected_result}, got: {actual_result}"
    else:
      print("Test passed")
    print("-" * 100)

if __name__ == "__main__":
  main()

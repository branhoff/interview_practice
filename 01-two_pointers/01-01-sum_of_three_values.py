def find_sum_of_three(nums, target):
  nums.sort()

  for i in range(0, len(nums) - 2):
    low = i + 1
    high = len(nums) - 1

    while low < high:
      triplet = nums[i] + nums[low] + nums[high]

      if triplet == target:
        return True

      elif triplet < target:
        low += 1

      else:
        high -= 1

  return False


# Driver code
def main():
  nums_lists = [
    [3, 7, 1, 2, 8, 4, 5],
    [-1, 2, 1, -4, 5, -3],
    [2, 3, 4, 1, 7, 9],
    [1, -1, 0],
    [2, 4, 2, 7, 6, 3, 1]
  ]

  targets = [10, 7, 20, -1, 8]

  expected_outcomes = [True, False, True, False, True]

  for i, (nums, target, expected) in enumerate(
      zip(nums_lists, targets, expected_outcomes), start=1):
    actual = find_sum_of_three(nums, target)
    print(f"{i}. Input array: {nums}")
    print(f"   Target sum: {target}")
    print(
      f"   Expected outcome: {'Sum exists' if expected else 'Sum does not exist'}")
    print(
      f"   Actual outcome: {'Sum exists' if actual else 'Sum does not exist'}")

    assert actual == expected, f"Test failed for input: {nums} with target {target}. Expected: {expected}, got: {actual}"
    print("-" * 100)

  print("All tests passed successfully!")


if __name__ == '__main__':
  main()

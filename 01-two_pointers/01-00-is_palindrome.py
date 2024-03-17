def is_palindrome(s):
  head = 0
  tail = len(s) - 1
  i = 0

  while i != len(s) // 2:
    if s[head] != s[tail]:
      return False
    else:
      head += 1
      tail -= 1
      i += 1

  return True


def solution(array):
  left = 0
  right = len(array) - 1

  while left <= right:
    if s[left] != s[right]:
      return False
    else:
      left = left + 1
      right = right - 1

  return True


def main():
  print(is_palindrome("kayak"))
  print(is_palindrome("hello"))
  print(is_palindrome("RACEACAR"))
  print(is_palindrome("A"))
  print(is_palindrome("ABCDABCD"))


if __name__ == "__main__":
  main()

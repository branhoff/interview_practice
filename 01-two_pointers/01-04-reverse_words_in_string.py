"""
This solution was originally based on the official solution of Grokking the Coding Interview.
It has been updated to not use the `re` library for cleaning out white space.
"""


def reverse_words(sentence):
  char_list = list(sentence)
  trim_spaces(char_list)

  str_len = len(char_list)

  reverse_segment(char_list, 0, str_len - 1)

  start = 0
  end = 0

  while (start < str_len):
    while end < str_len and char_list[end] != ' ':
      end += 1
    reverse_segment(char_list, start, end - 1)
    start = end + 1
    end += 1

  return ''.join(char_list)


def trim_spaces(char_list):
  while char_list and char_list[0] == " ":
    del char_list[0]

  while char_list and char_list[-1] == " ":
    del char_list[-1]

  index = 1
  while index < len(char_list):
    if char_list[index] == " " and char_list[index - 1] == " ":
      del char_list[index]
    else:
      index += 1


def reverse_segment(str_segment, start_rev, end_rev):
  while start_rev < end_rev:
    temp = str_segment[start_rev]
    str_segment[start_rev] = str_segment[end_rev]
    str_segment[end_rev] = temp

    start_rev += 1
    end_rev -= 1


def main():
  string_to_reverse = [
    "Hello Friend",
    "    We love Python",
    "The quick brown fox jumped over the lazy dog   ",
    "Hey",
    "To be or not to be",
    "AAAAA",
    "Hello     World"
  ]

  expected_results = [
    "Friend Hello",
    "Python love We",
    "dog lazy the over jumped fox brown quick The",
    "Hey",
    "be to not or be To",
    "AAAAA",
    "World Hello"
  ]

  for i, string in enumerate(string_to_reverse):
    actual_result = reverse_words(string)
    expected_result = expected_results[i]

    # Printing actual strings and their reversed versions for visual confirmation
    print(f"{i + 1}.\tActual string:\t\t{string}")
    print(f"\tReversed string:\t{actual_result}")
    print("-" * 100)

    # Assertion to check if the actual result matches the expected result
    assert actual_result == expected_result, f"Test failed for input: {string}. Expected: {expected_result}, got: {actual_result}"

  print("All tests passed successfully!")


if __name__ == '__main__':
  main()

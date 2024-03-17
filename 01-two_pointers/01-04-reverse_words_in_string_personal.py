def reverse_words(s):
  """
  output is wrong
  """
  output = []
  left = len(s)

  for i in range(len(s) - 1, -1, -1):
    if s[i] == " ":
      # Add the word if left index has moved from its initial position
      if left != len(s):
        output.append(s[i + 1:left])
      left = i  # Update left to the current space's index
    else:
      # If we're at the start of the string, ensure the first word is added
      if i == 0:
        output.append(s[i:left])

  # Join the words with a single space
  return " ".join(output)


# Driver code
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

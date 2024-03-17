RED = 0
WHITE = 1
BLUE = 2


def sort_colors(colors):
  red_ptr = 0
  white_ptr = 0
  blue_ptr = len(colors) - 1

  while white_ptr <= blue_ptr:
    if colors[white_ptr] == RED:
      colors[white_ptr], colors[red_ptr] = colors[red_ptr], colors[white_ptr]

      white_ptr += 1
      red_ptr += 1

    elif colors[white_ptr] == WHITE:
      white_ptr += 1

    elif colors[white_ptr] == BLUE:
      colors[white_ptr], colors[blue_ptr] = colors[blue_ptr], colors[white_ptr]
      blue_ptr -= 1

  return colors


# Driver code
def main():
  inputs = [
    [0, 1, 0],
    [1, 1, 0, 2],
    [2, 1, 1, 0, 0],
    [2, 2, 2, 0, 1, 0],
    [2, 1, 1, 0, 1, 0, 2],
  ]

  expected_outputs = [
    [0, 0, 1],
    [0, 1, 1, 2],
    [0, 0, 1, 1, 2],
    [0, 0, 1, 2, 2, 2],
    [0, 0, 1, 1, 1, 2, 2],
  ]

  for i, (input_colors, expected_output) in enumerate(
      zip(inputs, expected_outputs), start=1
  ):
    original_input = input_colors.copy()
    sorted_colors = sort_colors(input_colors)
    print(f"Test {i}:")
    print(f"Input: {original_input}")
    print(f"Expected Output: {expected_output}")
    print(f"Actual Output: {sorted_colors}")
    assert (
        sorted_colors == expected_output
    ), f"Test failed for input: {original_input}. Expected: {expected_output}, got: {sorted_colors}"
    print("-" * 50)

  print("All tests passed successfully!")


if __name__ == "__main__":
  main()

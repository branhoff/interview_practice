"""
## Repeated DNA Sequences
Given a string, `s`, that represents a DNA subsequence, and a number $k$,
return all the contiguous subsequences (substrings) of length $k$ that occur
more than once in the string. The order of the returned subsequences does not
matter. If no repeated substring is found, the function should return an empty
set.

> The DNA sequence is composed of a series of nucleotides abbreviated as
$A$, $C$, $G$, and $T$. For example, $ACGAATTCCG$ is a DNA sequence. When
studying DNA, it is useful to identify repeated sequences in it.

**Constraints**
- $1 \leq$ `s.length` $\leq 10^4$
- `s[i]` is either $A$, $C$, $G$, or $T$.
- $1 \leq k \leq 10$
"""

def find_repeated_sequences(string, k):
  # Define the size of the substring window.
  window_size = k
  # If the input string is shorter than the window size, return an empty set as
  # there can't be any repeats.
  if len(string) <= window_size:
    return set()

  # Define the base for the hash calculation. The choice of 4 corresponds to the
  # number of possible characters in 'mapping'.
  base = 4
  # Pre-calculate the high place value, which is used in the rolling hash
  # calculation.
  high_place_value = calculate_high_place_value(base, window_size)

  # Convert the input string into a numeric sequence based on a predefined
  # character mapping.
  mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
  numeric_sequence = convert_string_to_numeric_sequence(string, mapping)

  # Initialize the rolling hash value.
  hash_value = 0
  # Initialize sets for storing unique hash values of substrings and the output
  # set of repeated sequences.
  substring_hashes, output = set(), set()
  # Iterate over the string to examine all possible substrings of length 'k'.
  for start in range(len(string) - window_size + 1):
    if start != 0:
      # Update the hash value using the rolling hash method: remove the leftmost
      # character's contribution, shift, and add the new character's contribution.
      hash_value = (hash_value - numeric_sequence[start - 1] * high_place_value) * base + numeric_sequence[start + window_size - 1]
    else:
      # For the first window, calculate the hash value from scratch.
      for end in range(window_size):
        hash_value = hash_value * base + numeric_sequence[end]
    # Check if the current hash value has been seen before; if so, add the
    # corresponding substring to the output set.
    if hash_value in substring_hashes:
      output.add(string[start:start + window_size])
    # Add the current hash value to the set of seen hashes.
    substring_hashes.add(hash_value)
  return output

def calculate_high_place_value(base, window_size):
  # Calculate the high place value for the base raised to the power of
  # (window_size - 1).
  high_place_value = 1
  for _ in range(window_size - 1):
    high_place_value *= base
  return high_place_value

def convert_string_to_numeric_sequence(string, mapping):
  # Convert each character in the string to its numeric representation according
  # to the provided mapping.
  numeric_sequence = []
  for i in range(len(string)):
    numeric_sequence.append(mapping.get(string[i], 0))  # Use 0 as a default value if character is not found in mapping.
  return numeric_sequence


def main():
  inputs_string = ["ACGT", "AGACCTAGAC", "AAAAACCCCCAAAAACCCCCC",
                   "GGGGGGGGGGGGGGGGGGGGGGGGG",
                   "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT", "TTTTTGGGTTTTCCA",
                   "AAAAAACCCCCCCAAAAAAAACCCCCCCTG", "ATATATATATATATAT"]
  inputs_k = [3, 3, 8, 12, 10, 14, 10, 6]

  expected_outputs = [
    set(),
    {'GAC', 'AGA'},
    {'AAACCCCC', 'AAAACCCC', 'AAAAACCC'},
    {'GGGGGGGGGGGG'},
    {'CCCCCCCTTT', 'CCCCTTTTTT', 'TCCCCCCCTT', 'TTCCCCCCCT', 'TTTTCCCCCC',
     'TTTTTCCCCC', 'CCCCCCTTTT', 'CCCCCTTTTT', 'TTTCCCCCCC'},
    set(),
    {'AAAAACCCCC', 'AAACCCCCCC', 'AAAAAACCCC', 'AAAACCCCCC'},
    {'ATATAT', 'TATATA'}
                     ]

  for i in range(len(inputs_k)):
    print(i + 1, ".\tInput Sequence: \'", inputs_string[i], "\'", sep="")
    print("\tk: ", inputs_k[i], sep="")
    actual_result =  find_repeated_sequences(inputs_string[i], inputs_k[i])
    print("\tOutputted Subsequence: ", actual_result)
    if actual_result != expected_outputs[i]:
      print(
        f"Test failed. Expected: {expected_outputs[i]}, got: {actual_result}")
    else:
      print("Test passed.")
    print("-" * 100)


if __name__ == '__main__':
  main()

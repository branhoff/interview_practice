"""
We are given an array of closed intervals, intervals, where each interval has a
start time and an end time. The input array is sorted with respect to the start
times of each interval. For example,
intervals = [ [1,4], [3,6], [7,9] ] is sorted in terms of
start times 1, 3 and 7.

Your task is to merge the overlapping intervals and return a new output array
consisting of only the non-overlapping intervals.

Constraints:
- $1 \leq$ `intervals.length` $\leq 10^4$
- intervals[i].length1 $=2$
- $0\leq$ start time $\leq$ end time $\leq 10^4$
"""


def merge_intervals(intervals):
  if not intervals:
    return None
  result = []
  result.append([intervals[0][0], intervals[0][1]])
  for i in range(1, len(intervals)):
    last_added_interval = result[len(result) - 1]
    curr_start = intervals[i][0]
    curr_end = intervals[i][1]
    prev_end = last_added_interval[1]

    if curr_start <= prev_end:
      result[-1][1] = max(curr_end, prev_end)
    else:
      result.append([curr_start, curr_end])
  return result


# Driver code
def main():
  all_intervals = [
    [[1, 5], [3, 7], [4, 6]],
    [[1, 5], [4, 6], [6, 8], [11, 15]],
    [[3, 7], [6, 8], [10, 12], [11, 15]],
    [[1, 5]],
    [[1, 9], [3, 8], [4, 4]],
    [[1, 2], [3, 4], [8, 8]],
    [[1, 5], [1, 3]],
    [[1, 5], [6, 9]],
    [[0, 0], [1, 18], [1, 3]]
  ]

  expected_outputs = [
    [[1, 7]],
    [[1, 8], [11, 15]],
    [[3, 8], [10, 15]],
    [[1, 5]],
    [[1, 9]],
    [[1, 2], [3, 4], [8, 8]],
    [[1, 5]],
    [[1, 5], [6, 9]],
    [[0, 0], [1, 18]]

  ]

  for i in range(len(all_intervals)):
    print(i + 1, ". Intervals to merge: ", all_intervals[i], sep="")
    result = merge_intervals(all_intervals[i])
    print("   Merged intervals:\t", result)
    if result != expected_outputs[i]:
      print("Failed, result does not match the expected output.")
    else:
      print("Test passed.")
    print("-" * 100)


if __name__ == '__main__':
  main()

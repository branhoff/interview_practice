def smallest_subbarray_with_greater_sum(s, arr):
    solution = 0

    window_sum = 0

    for i in range(len(arr)):
        for window_end in range(len(arr)):
            window_sum += arr[window_end]


            if window_sum >= s:
                solution = i + 1
                return solution

            if window_end >= i:
                window_sum -= arr[window_end - i]
    
    return solution


def main():
    s = 7
    result = smallest_subbarray_with_greater_sum(s, [2, 1, 5, 2, 3, 2])
    print(f"The smallest continguous subarray with a sum greater than or equal to '{s}'': " + str(result))

    s = 7
    result = smallest_subbarray_with_greater_sum(s, [2, 1, 5, 2, 8])
    print(f"The smallest continguous subarray with a sum greater than or equal to '{s}'': " + str(result))

    s = 8
    result = smallest_subbarray_with_greater_sum(s, [3, 4, 1, 1, 6])
    print(f"The smallest continguous subarray with a sum greater than or equal to '{s}'': " + str(result))


main()


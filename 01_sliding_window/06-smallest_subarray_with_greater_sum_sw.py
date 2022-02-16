


def smallest_subbarray_with_greater_sum(s, arr):
    min_arr_len = 0

    window_start = 0
    window_sum = 0
    

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        window_len = window_end - window_start + 1

    
        while window_sum >= s:
            if min_arr_len == 0:
                min_arr_len = window_len
            min_arr_len = min(min_arr_len, window_len)
            window_sum -= arr[window_start]
            window_start += 1
            window_len = window_end - window_start + 1


    return min_arr_len

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

    # Time Complesity of the above Algorithim will be O(N). The outer for loop runs for all elements
    # and the inner while loop processes each element only once; therefore, the time complexity of the algorithm will be
    # O(N + N), which is asymptotically equivalent to O(N).
    
    # Space Complexity runs in constant space O(1)

main()


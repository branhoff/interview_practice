def max_sub_array_of_size_k(k, arr):
    max_sum = 0
    window_sum = 0
    window_start = 0
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end] # add the next element

        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if window_end >= k-1:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[window_start] # subtract the element going out
            window_start += 1 # slide the window ahead
        
    return max_sum


def main():
    k = 3
    result = max_sub_array_of_size_k(k, [2, 1, 5, 1, 3, 2])
    print(f"Max of subarray of size {k}: " + str(result))

    k = 2
    result = max_sub_array_of_size_k(k, [2, 3, 4, 1, 5])
    print(f"Max of subarray of size {k}: " + str(result))

    # Time Complesity of the above Algorithim will be O(N)
    # Space Complexity runs in constant space O(1)


main()
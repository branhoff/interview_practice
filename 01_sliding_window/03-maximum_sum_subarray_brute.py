def max_sub_array_of_size_k(k, arr):
    max_sum = 0
    
    for i in range(len(arr)-k):
        sum_ = 0
        for j in range(i, i+k):
            sum_ += arr[j]
        
        max_sum = max(max_sum, sum_)
        
    return max_sum


def main():
    k = 3
    result = max_sub_array_of_size_k(k, [2, 1, 5, 1, 3, 2])
    print(f"Max of subarray of size {k}: " + str(result))

    k = 2
    result = max_sub_array_of_size_k(k, [2, 3, 4, 1, 5])
    print(f"Max of subarray of size {k}: " + str(result))


main()
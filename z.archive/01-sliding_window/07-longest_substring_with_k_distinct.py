# Solution is a bit different than official solution. Consider changing


def longest_substring_with_k_distinct(str1, k):

    window_start = 0
    longest_substring = 0
    char_frequency = dict()
    
    for window_end in range(len(str1)):
        latest_char = str1[window_end]
        
        if latest_char not in char_frequency:
            char_frequency[latest_char] = 1
        else:
            char_frequency[latest_char] += 1

        if len(char_frequency) <= k:
            longest_substring = max(longest_substring, window_end - window_start + 1)

        while len(char_frequency) > k:
            earliest_char = str1[window_start]
            
            try:
                if earliest_char in char_frequency:
                    char_frequency[earliest_char] -=1
                
                if char_frequency[earliest_char] == 0:
                    char_frequency.pop(earliest_char)
            except KeyError:
                pass

            window_start += 1

    return longest_substring


        

    

def main():
    k = 2
    result = longest_substring_with_k_distinct("araaci", k)
    print(f"The smallest continguous subarray with a sum greater than or equal to '{k}'': " + str(result))
    
    k = 1
    result = longest_substring_with_k_distinct("araaci", k)
    print(f"The smallest continguous subarray with a sum greater than or equal to '{k}'': " + str(result))

    k = 3
    result = longest_substring_with_k_distinct("cbbebi", k)
    print(f"The smallest continguous subarray with a sum greater than or equal to '{k}'': " + str(result))

    k = 10
    result = longest_substring_with_k_distinct("cbbebi", k)
    print(f"The smallest continguous subarray with a sum greater than or equal to '{k}'': " + str(result))

    # Time Complexity will be O(N). The outer for loop runs for all character, and the inner while loop processes
    # each character only once; therefore, the time complexity of the algorithm will be O(N + N), which is asymptotically
    # equivalent to O(N)

    # Space Complexity is O(K), as we will be storing a maximum of K+1 characters in the HashMap

main()


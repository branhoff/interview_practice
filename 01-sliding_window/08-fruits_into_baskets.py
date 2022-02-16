# You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

#     1. Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
#     2. You can start with any tree, but you can’t skip a tree once you have started.
#     3. You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both baskets.


def fruits_into_baskets(fruits):
    '''input: array of chars
       output: int represents longest sequence with only two fruits'''

    fruit_frequencey = {}
    max_fruit = 0
    window_start = 0

    for window_end in range(len(fruits)):
        head_char = fruits[window_end]

        if head_char not in fruit_frequencey:
            fruit_frequencey[head_char] = 1
        else:
            fruit_frequencey[head_char] += 1

        

        while len(fruit_frequencey) > 2:
            tail_char = fruits[window_start]

            fruit_frequencey[tail_char] -= 1

            if fruit_frequencey[tail_char] == 0:
                fruit_frequencey.pop(tail_char)
        
            window_start += 1
        
        max_fruit = max(sum(fruit_frequencey.values()), max_fruit)

    return max_fruit

def main():
    result = fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])
    print(f"Maximum number of only two fruits: " + str(result))

    result = fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])
    print(f"Maximum number of only two fruits: " + str(result))


if __name__ == "__main__":
    main()
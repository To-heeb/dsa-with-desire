def fruits_into_baskets(fruits) -> int:
    window_start = 0
    max_length = 0
    char_frequency = {}

    for window_end in range(len(fruits)):
        rightmost_char = fruits[window_end]
        if rightmost_char not in char_frequency:
            char_frequency[rightmost_char] = 0
        char_frequency[rightmost_char] += 1
        
        while len(char_frequency) > 2:
            leftmost_char = fruits[window_start]
            
            char_frequency[leftmost_char] -= 1
            if char_frequency[leftmost_char] == 0:
                del char_frequency[leftmost_char]
            window_start += 1
        
        max_length = max(max_length, (window_end - window_start) + 1)

    return max_length


def main():
    result1 = fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])
    result2 = fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])
    print("Maximum number of fruits: " + str(result1))
    print("Maximum number of fruits: " + str(result2))


main()

def longest_substring_with_k_distinct(string, k):
    window_start = 0
    max_length = 0
    char_frequency = {}

    for window_end in range(len(string)):
        rightmost_char = string[window_end]
        if rightmost_char not in char_frequency:
            char_frequency[rightmost_char] = 0
        char_frequency[rightmost_char] += 1

        while len(char_frequency) > k:
            leftmost_char = string[window_start]
            char_frequency[leftmost_char] -= 1
            if char_frequency[leftmost_char] == 0:
                del char_frequency[leftmost_char]
            window_start += 1

        max_length = max(max_length, (window_end - window_start) + 1)

    return max_length


def main():
    result1 = longest_substring_with_k_distinct("araaci", 2)
    result2 = longest_substring_with_k_distinct("araaci", 1)
    result3 = longest_substring_with_k_distinct("cbbebi", 3)
    print("Length of the longest substring: " + str(result1))
    print("Length of the longest substring: " + str(result2))
    print("Length of the longest substring: " + str(result3))


main()

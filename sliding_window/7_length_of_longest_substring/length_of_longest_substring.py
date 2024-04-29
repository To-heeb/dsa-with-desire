def length_of_longest_substring(string, k) -> int:
    window_start = 0
    max_repeating_char = 0
    longest_repeating_substring_k_replacement = 0
    char_frequency = {}

    for window_end in range(len(string)):
        rightmost_char = string[window_end]
        if rightmost_char not in char_frequency:
            char_frequency[rightmost_char] = 0
        char_frequency[rightmost_char] += 1

        max_repeating_char = max(max_repeating_char,
                                 char_frequency[rightmost_char])

        window_range = (window_end - window_start) + 1

        while window_range > (max_repeating_char + k):
            leftmost_char = string[window_start]
            char_frequency[leftmost_char] -= 1
            window_start += 1
            window_range = (window_end - window_start) + 1

        longest_repeating_substring_k_replacement = max(
            longest_repeating_substring_k_replacement, (window_end - window_start) + 1)

    return longest_repeating_substring_k_replacement


def main():
    result1 = length_of_longest_substring("aabccbb", 2)
    result2 = length_of_longest_substring("abbcb", 1)
    result3 = length_of_longest_substring("abccde", 1)
    print("Length of the longest substring: " + str(result1))
    print("Length of the longest substring: " + str(result2))
    print("Length of the longest substring: " + str(result3))


main()

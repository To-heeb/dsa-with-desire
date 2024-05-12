def non_repeat_substring(string):
    window_start = 0
    max_length_with_no_repeating_char = 0
    char_frequency = {}

    for window_end in range(len(string)):
        rightmost_char = string[window_end]
        if rightmost_char not in char_frequency:
            char_frequency[rightmost_char] = 0
        char_frequency[rightmost_char] += 1

        while char_frequency[rightmost_char] > 1:
            leftmost_char = string[window_start]
            char_frequency[leftmost_char] -= 1
            window_start += 1

        max_length_with_no_repeating_char = max(
            max_length_with_no_repeating_char, (window_end - window_start) + 1)

    return max_length_with_no_repeating_char


def main():
    result1 = non_repeat_substring("aabccbb")
    result2 = non_repeat_substring("abbbb")
    result3 = non_repeat_substring("abccde")
    print("Maximum number of fruits: " + str(result1))
    print("Maximum number of fruits: " + str(result2))
    print("Maximum number of fruits: " + str(result3))


main()

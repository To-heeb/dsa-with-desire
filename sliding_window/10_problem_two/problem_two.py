def find_string_anagrams(string, pattern):
    window_start = 0
    results = []
    char_frequency = {}

    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1

    for window_end in range(len(string)):
        matches = 0
        char_frequency_copy = char_frequency.copy()
        temp_start = window_start

        window_range = (window_end - window_start) + 1
        while window_range >= len(pattern):
            leftmost_char = string[temp_start]
            if leftmost_char not in char_frequency_copy:
                window_start += 1
                break
            if leftmost_char in char_frequency_copy:
                char_frequency_copy[leftmost_char] -= 1
                if char_frequency_copy[leftmost_char] == 0:
                    del char_frequency_copy[leftmost_char]
                temp_start += 1
                matches += 1

            if matches == len(pattern):
                results += [window_start]
                window_start += 1
                window_range = (window_end - window_start) + 1
            # print(char_frequency_copy, window_start, leftmost_char)
    return results


def main():
    result1 = find_string_anagrams("ppqp", "pq")
    result2 = find_string_anagrams("abbcabc", "abc")
    print("Permutation exists in indexes:  " + str(result1))
    print("Permutation exists in indexes:  " + str(result2))


main()

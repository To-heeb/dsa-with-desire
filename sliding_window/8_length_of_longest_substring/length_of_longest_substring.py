def length_of_longest_substring(arr, k) -> int:
    window_start = 0
    max_ones_count = 0
    max_length = 0
    num_frequency = [0, 0]

    for window_end in range(len(arr)):
        rightmost_num = arr[window_end]
        num_frequency[rightmost_num] += 1

        if rightmost_num == 1:
            max_ones_count += 1

        window_range = (window_end - window_start) + 1

        if window_range > (max_ones_count + k):
            leftmost_num = arr[window_start]
            num_frequency[leftmost_num] -= 1

            if leftmost_num == 1:
                max_ones_count -= 1
            window_start += 1

        max_length = max(max_length, (window_end - window_start) + 1)

    return max_length


def main():
    result1 = length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2)
    result2 = length_of_longest_substring(
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3)
    print("Length of the longest substring: " + str(result1))
    print("Length of the longest substring: " + str(result2))


main()

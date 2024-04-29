def smallest_subarray_with_given_sum(arr, S) -> int:
    window_start = 0
    min_length = len(arr) + 1
    window_end = 0
    window_sum = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= S:
            window_range = (window_end - window_start) + 1
            min_length = min(min_length, window_range)
            window_sum -= arr[window_start]
            window_start += 1

    if min_length == len(arr) + 1:
        min_length = 0

    return min_length


def main():
    result1 = smallest_subarray_with_given_sum([2, 1, 5, 2, 3, 2], 7)
    result2 = smallest_subarray_with_given_sum([2, 1, 5, 2, 8], 7)
    result3 = smallest_subarray_with_given_sum([3, 4, 1, 1, 6], 8)
    print("Smallest subarray length: " + str(result1))
    print("Smallest subarray length: " + str(result2))
    print("Smallest subarray length: " + str(result3))


main()

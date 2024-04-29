
def maximum_sum_subarray_of_size_k(arr, k):
    """
Find the maximum sum of a subarray of size k in the given array.

Parameters:
- arr (List[int]): The input array.
- k (int): The size of the subarray.

Returns:
- int: The maximum sum of a subarray of size k.
"""
    window_start = 0
    window_sum = 0
    maximum_sum = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        window_range = (window_end - window_start) + 1
        if window_range >= k:
            maximum_sum = max(maximum_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1

    return maximum_sum


def main():
    result1 = maximum_sum_subarray_of_size_k([2, 1, 5, 1, 3, 2], 3)
    result2 = maximum_sum_subarray_of_size_k([2, 3, 4, 1, 5], 2)
    print("Maximum sum of a subarray of size K: " + str(result1))
    print("Maximum sum of a subarray of size K: " + str(result2))


main()

# def find_averages_of_subarrays_of_size_k_O_n_k(arr, k):


def find_averages_of_subarrays_of_size_k_O_n(arr, k):
    """
Find the averages of subarrays of size k in the given array.

Args:
- arr (List[int]): The input array.
- k (int): The size of the subarray.

Returns:
- List[float]: The averages of subarrays of size k.
"""

    window_start = 0
    result = []
    window_sum = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        window_range = (window_end - window_start) + 1
        if window_range >= k:
            result += [window_sum / k]
            window_sum -= arr[window_start]
            window_start += 1
            window_range = (window_end - window_start) + 1
    return result


def main():
    """
Executes the main function.

This function calculates the averages of subarrays of size k in the given array. 
It takes no parameters.

Returns:
    None
"""
    result1 = find_averages_of_subarrays_of_size_k_O_n(
        [1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
    # result2 = find_averages_of_subarrays_of_size_k_O_n_k(
    #     [1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
    print("Averages of subarrays of size K: " + str(result1))
    # print("Averages of subarrays of size K: " + str(result2))


main()

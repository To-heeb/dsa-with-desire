def find_permutation(string, pattern) -> bool:
    window_start = 0

    for window_end in range(len(string)):
        matches = 0

        window_range = (window_end - window_start) + 1
        while window_range >= len(pattern):
            leftmost_char = string[window_start]
            if leftmost_char not in pattern:
                window_start += 1
                break
            if leftmost_char in pattern:
                matches += 1
                window_start += 1
            if matches == len(pattern):
                return True

    return False


def main():
    result1 = find_permutation("oidbcaf", "abc")
    result2 = find_permutation("odicf", "dc")
    result3 = find_permutation("bcdxabcdy", "bcdyabcdx")
    result4 = find_permutation("aaacb", "abc")
    result5 = find_permutation("ppq", "pq")
    print("Permutation exist:  " + str(result1))
    print("Permutation exist:  " + str(result2))
    print("Permutation exist:  " + str(result3))
    print("Permutation exist:  " + str(result4))
    print("Permutation exist:  " + str(result5))


main()

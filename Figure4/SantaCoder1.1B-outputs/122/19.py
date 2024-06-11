def add_elements(arr, k):
    
    # Runtime: 128 ms, faster than 81.47% of Python3 online submissions for Sum of Two Digits In First K Numbers.
    # Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Sum of Two Digits In First K Numbers.
    return sum(arr[:k]) + sum(arr[k:])


if __name__ == "__main__":
    arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k = 4
    print(add_elements(arr, k))

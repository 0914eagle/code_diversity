def add_elements(arr, k):
    
    # Runtime: 28 ms, faster than 93.09% of Python3 online submissions for Sum of Two Elements with At Most Two Digits.
    # Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Sum of Two Elements with At Most Two Digits.
    # Time complexity: O(n)
    # Space complexity: O(1)
    return sum(arr[:k]) + sum(arr[k:])



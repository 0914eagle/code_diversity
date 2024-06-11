def smallest_change(arr):
    
    # Your code here
    # 1. find the longest palindromic subsequence
    # 2. subtract the length of the longest palindromic subsequence from the length of the array
    # 3. return the result
    # 4. if the array is already a palindrome, return 0
    # 5. if the array is empty, return 0

    if len(arr) == 0:
        return 0

    if is_palindrome(arr):
        return 0

    return len(arr) - longest_palindromic_subsequence(arr)



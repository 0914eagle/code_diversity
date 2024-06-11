def smallest_change(arr):
    
    if is_palindrome(arr):
        return 0
    else:
        return 1 + smallest_change(arr[1:-1])



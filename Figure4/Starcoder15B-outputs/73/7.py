def smallest_change(arr):
    
    # Your code here
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        return 1 if arr[0] != arr[1] else 0
    if len(arr) == 3:
        return 1 if arr[0] == arr[2] else 2
    if len(arr) == 4:
        return 2 if arr[0] == arr[3] and arr[1] == arr[2] else 1

    if is_palindrome(arr):
        return 0

    if is_palindrome(arr[1:]):
        return 1

    if is_palindrome(arr[:-1]):
        return 1

    if is_palindrome(arr[2:-2]):
        return 2

    if is_palindrome(arr[1:-1]):
        return 2

    if is_palindrome(arr[2:-1]):
        return 2

    if is_palindrome(arr[1:-2]):
        return 2

    if is_palindrome(arr[2:]):
        return 1

    if is_palindrome(arr[:-2]):
        return 1

    if is_palindrome(arr[3:-3]):
        return 2

    if is_palindrome(arr[3:]):
        return 1

    if is_palindrome(arr[:-3]):
        return 1

    if is_palindrome(arr[4:-4]):
        return 2

    if is_palindrome(arr[4:]):
        return 1

    if is_palindrome(arr[:-4]):
        return 1

    if is_palindrome(arr[5:-5]):
        return 2

    if is_palindrome(arr[5:]):
        return 1

    if is_palindrome(arr[:-5]):
        return 1

    if is_palindrome(arr[6:-6]):
        return 2

    if is_palindrome(arr[6:]):
        return 1

    if is_palindrome(arr[:-6]):
        return 1

    if is_palindrome(arr[7:-7]):
        return 2

    if is_palindrome(arr[7:]):
        return 1

    if is_palindrome(arr[:-7]):
        return 1

    if is_pal
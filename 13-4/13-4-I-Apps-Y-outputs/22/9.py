
def is_palindrome(arr):
    # Check if the array is a palindrome
    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - i - 1]:
            return False
    return True

def has_subsequence_palindrome(arr, n):
    # Check if the array has a subsequence of length at least 3 that is a palindrome
    for i in range(len(arr) - 2):
        subarr = arr[i:i+n]
        if is_palindrome(subarr):
            return True
    return False

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print("YES") if has_subsequence_palindrome(arr, 3) else print("NO")


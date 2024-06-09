
def check_palindrome(arr):
    # Check if array is a palindrome
    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - i - 1]:
            return False
    return True

def check_subsequence_palindrome(arr, n):
    # Check if there is a subsequence of length n that is a palindrome
    for i in range(len(arr) - n + 1):
        subarr = arr[i:i+n]
        if check_palindrome(subarr):
            return True
    return False

def solve(arr):
    # Check if there is a subsequence of length at least 3 that is a palindrome
    for i in range(3, len(arr) + 1):
        if check_subsequence_palindrome(arr, i):
            return "YES"
    return "NO"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))



def is_palindrome(arr):
    # Check if the array is a palindrome
    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - i - 1]:
            return False
    return True

def has_palindromic_subsequence(arr, n):
    # Check if the array has a subsequence of length at least n that is a palindrome
    for i in range(len(arr) - n + 1):
        subarr = arr[i:i+n]
        if is_palindrome(subarr):
            return True
    return False

def main():
    num_test_cases = int(input())
    for i in range(num_test_cases):
        n = int(input())
        arr = list(map(int, input().split()))
        print("YES") if has_palindromic_subsequence(arr, 3) else print("NO")

if __name__ == '__main__':
    main()


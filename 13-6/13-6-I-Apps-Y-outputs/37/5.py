
def check_palindrome(arr):
    # Check if the array is a palindrome
    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - i - 1]:
            return False
    return True

def check_subsequence(arr, sub):
    # Check if the subsequence is in the array
    for i in range(len(arr) - len(sub) + 1):
        if arr[i:i+len(sub)] == sub:
            return True
    return False

def has_palindromic_subsequence(arr):
    # Check if the array has a subsequence of length at least 3 that is a palindrome
    for i in range(len(arr) - 2):
        for j in range(i+1, len(arr) - 1):
            sub = arr[i:j+1]
            if check_palindrome(sub) and check_subsequence(arr, sub):
                return True
    return False

def main():
    tests = int(input())
    for i in range(tests):
        n = int(input())
        arr = list(map(int, input().split()))
        if has_palindromic_subsequence(arr):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()


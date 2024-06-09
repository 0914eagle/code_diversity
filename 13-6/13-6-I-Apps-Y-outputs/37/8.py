
def is_palindrome(arr):
    # Check if the array is a palindrome
    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - i - 1]:
            return False
    return True

def has_subsequence_of_length_at_least_3(arr):
    # Check if the array has a subsequence of length at least 3
    for i in range(len(arr) - 2):
        if is_palindrome(arr[i:i+3]):
            return True
    return False

def main():
    num_test_cases = int(input())
    for i in range(num_test_cases):
        n = int(input())
        arr = list(map(int, input().split()))
        if has_subsequence_of_length_at_least_3(arr):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()


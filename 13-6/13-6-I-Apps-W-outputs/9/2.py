
def get_input():
    n = int(input())
    arr = list(map(int, input().split()))
    return n, arr

def solve(n, arr):
    # Initialize the maximum sum to 0
    max_sum = 0
    # Loop through each element in the array
    for i in range(n):
        # Calculate the sum of the elements to the left and right of the current element
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i+1:])
        # If the sum of the elements to the left and right of the current element is greater than the maximum sum, update the maximum sum
        if left_sum + right_sum > max_sum:
            max_sum = left_sum + right_sum
    # Return the maximum sum
    return max_sum

def main():
    n, arr = get_input()
    print(solve(n, arr))

if __name__ == '__main__':
    main()


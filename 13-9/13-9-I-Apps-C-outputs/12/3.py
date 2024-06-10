
def get_maximum_sum(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the maximum sum to be 0
    max_sum = 0
    # Loop through the array and calculate the sum
    for i in range(len(arr)):
        max_sum += arr[i]
    # Return the maximum sum
    return max_sum

def get_maximum_sum_with_operations(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the maximum sum to be 0
    max_sum = 0
    # Loop through the array and calculate the sum
    for i in range(len(arr)):
        max_sum += arr[i]
    # Return the maximum sum
    return max_sum

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(get_maximum_sum_with_operations(arr))



def get_min_sum(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the sum of non-deleted elements
    sum_non_deleted = 0
    # Initialize the number of moves
    num_moves = 0
    # Loop through the array
    for i in range(len(arr)):
        # Check if the current element is even
        if arr[i] % 2 == 0:
            # If the current element is even and the number of moves is odd, delete the current element
            if num_moves % 2 == 1:
                sum_non_deleted += arr[i]
            # Increment the number of moves
            num_moves += 1
        # If the current element is odd
        else:
            # If the current element is odd and the number of moves is even, delete the current element
            if num_moves % 2 == 0:
                sum_non_deleted += arr[i]
            # Increment the number of moves
            num_moves += 1
    # Return the minimum possible sum of non-deleted elements
    return sum_non_deleted

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_min_sum(arr))


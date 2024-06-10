
def get_min_moves(arr, k):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the number of moves to 0
    moves = 0
    # Initialize the number of equal elements to 0
    equal_elements = 0
    # Loop through the array
    for i in range(len(arr)):
        # If the current element is equal to the previous element, increment the number of equal elements
        if i > 0 and arr[i] == arr[i-1]:
            equal_elements += 1
        # If the number of equal elements is greater than or equal to k, return the number of moves
        if equal_elements >= k:
            return moves
        # If the current element is not equal to the previous element, increment the number of moves
        if i == 0 or arr[i] != arr[i-1]:
            moves += 1
    # If the number of equal elements is less than k, return -1
    return -1

def solve(n, k, arr):
    # Call the get_min_moves function and return the result
    return get_min_moves(arr, k)

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n, k, arr))



def f1(n, arr):
    # Sort the array in non-descending order
    arr.sort()
    # Initialize the number of swaps to 0
    swaps = 0
    # Loop through the array and check if it is sorted
    for i in range(n-1):
        # If the array is not sorted, increment the number of swaps
        if arr[i] > arr[i+1]:
            swaps += 1
    # Return the number of swaps
    return swaps

def f2(n, arr):
    # Sort the array in non-descending order
    arr.sort()
    # Initialize the number of swaps to 0
    swaps = 0
    # Loop through the array and check if it is sorted
    for i in range(n-1):
        # If the array is not sorted, increment the number of swaps
        if arr[i] > arr[i+1]:
            swaps += 1
            # Swap the elements
            arr[i], arr[i+1] = arr[i+1], arr[i]
    # Return the number of swaps
    return swaps, arr

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    swaps = f1(n, arr)
    print(swaps)
    swaps, arr = f2(n, arr)
    print(swaps)
    for i in range(n):
        print(arr[i], end=" ")


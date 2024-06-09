
def get_min_d(arr):
    # Sort the array in ascending order
    arr.sort()
    
    # Initialize the minimum difference between elements as the difference between the first two elements
    min_d = arr[1] - arr[0]
    
    # Iterate through the array and calculate the difference between each element and the previous element
    for i in range(1, len(arr)):
        d = arr[i] - arr[i-1]
        
        # If the difference is less than the minimum difference, update the minimum difference
        if d < min_d:
            min_d = d
    
    return min_d

def get_equal_array(arr, d):
    # Add d to the first element of the array
    arr[0] += d
    
    # Iterate through the array and subtract d from each element
    for i in range(1, len(arr)):
        arr[i] -= d
    
    return arr

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Get the minimum difference between elements in the array
    d = get_min_d(arr)
    
    # Check if the minimum difference is non-negative
    if d >= 0:
        # Add the minimum difference to the first element of the array and subtract it from the other elements
        arr = get_equal_array(arr, d)
        print(d)
    else:
        print(-1)

if __name__ == '__main__':
    main()


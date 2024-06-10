
def get_sorted_ranges(arr, x):
    # Initialize a dictionary to store the count of sorted ranges
    sorted_ranges = {}
    
    # Iterate over the array and count the number of sorted ranges
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] <= arr[j]:
                sorted_ranges[(i, j)] = 1
    
    # Return the number of sorted ranges
    return len(sorted_ranges)

def main():
    # Read the input data
    n, x = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    
    # Calculate the number of sorted ranges
    sorted_ranges = get_sorted_ranges(arr, x)
    
    # Print the result
    print(sorted_ranges)

if __name__ == '__main__':
    main()


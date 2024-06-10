
def get_sorted_ranges(arr, x):
    # Initialize a dictionary to store the count of sorted ranges
    sorted_ranges = {}

    # Iterate over the array
    for i in range(len(arr)):
        # Get the current element
        curr = arr[i]

        # Iterate over the range of values from 1 to x
        for j in range(1, x + 1):
            # Check if the current element is less than or equal to j
            if curr <= j:
                # Increment the count of sorted ranges for the current element
                sorted_ranges[j] = sorted_ranges.get(j, 0) + 1

    # Initialize a variable to store the total number of sorted ranges
    total_sorted_ranges = 0

    # Iterate over the sorted ranges
    for k, v in sorted(sorted_ranges.items()):
        # Check if the count of sorted ranges is greater than or equal to k
        if v >= k:
            # Increment the total number of sorted ranges
            total_sorted_ranges += 1

    # Return the total number of sorted ranges
    return total_sorted_ranges

def main():
    # Read the input
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    # Call the get_sorted_ranges function
    total_sorted_ranges = get_sorted_ranges(arr, x)

    # Print the total number of sorted ranges
    print(total_sorted_ranges)

if __name__ == '__main__':
    main()



def get_divisible_elements(arr):
    # Count the number of elements divisible by 3 in the array
    count = 0
    for num in arr:
        if num % 3 == 0:
            count += 1
    return count

def get_max_divisible_elements(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the maximum number of elements divisible by 3 to 0
    max_count = 0
    # Loop through the array and try all possible pairs of elements
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            # Check if the sum of the two elements is divisible by 3
            if (arr[i] + arr[j]) % 3 == 0:
                # If the sum is divisible by 3, add it to the array and sort it
                arr.append(arr[i] + arr[j])
                arr.sort()
                # Get the number of elements divisible by 3 in the array
                count = get_divisible_elements(arr)
                # Update the maximum number of elements divisible by 3 if necessary
                max_count = max(max_count, count)
                # Remove the last element from the array
                arr.pop()
    return max_count

def main():
    # Read the number of queries
    t = int(input())
    # Loop through each query
    for _ in range(t):
        # Read the size of the array
        n = int(input())
        # Read the array
        arr = list(map(int, input().split()))
        # Get the maximum number of elements divisible by 3 in the array
        max_count = get_max_divisible_elements(arr)
        # Print the result
        print(max_count)

if __name__ == '__main__':
    main()


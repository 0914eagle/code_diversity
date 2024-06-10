
def get_min_length(arr):
    # Initialize a variable to keep track of the minimum length
    min_length = len(arr)
    # Loop through the array and check if there are any adjacent elements that are equal
    for i in range(len(arr) - 1):
        # If the current element is equal to the next element, replace them with the sum of the two elements plus 1
        if arr[i] == arr[i + 1]:
            arr[i] = arr[i] + arr[i + 1] + 1
            # Remove the next element from the array
            arr.pop(i + 1)
            # Decrement the minimum length by 1
            min_length -= 1
    # Return the minimum length
    return min_length

def main():
    # Read the input
    n = int(input())
    arr = list(map(int, input().split()))
    # Get the minimum length
    min_length = get_min_length(arr)
    # Print the minimum length
    print(min_length)

if __name__ == '__main__':
    main()


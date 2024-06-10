
def get_min_length(arr):
    # Sort the array in ascending order
    arr.sort()
    # Initialize a variable to store the minimum length
    min_length = len(arr)
    # Loop through the array and check for adjacent equal elements
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            # If there are adjacent equal elements, replace them with one element with value arr[i] + 1
            arr[i] = arr[i] + 1
            # Remove the next element
            arr.pop(i + 1)
            # Decrement the minimum length by 1
            min_length -= 1
    return min_length

def main():
    # Read the input array
    n = int(input())
    arr = list(map(int, input().split()))
    # Get the minimum length of the array
    min_length = get_min_length(arr)
    # Print the minimum length
    print(min_length)

if __name__ == '__main__':
    main()


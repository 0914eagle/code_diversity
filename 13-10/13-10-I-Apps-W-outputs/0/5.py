
def min_length(arr):
    # Sort the array in descending order
    arr.sort(reverse=True)
    # Initialize a counter for the length of the array
    length = len(arr)
    # Loop through the array and check for adjacent elements that are equal
    for i in range(length-1):
        if arr[i] == arr[i+1]:
            # If we find a pair of adjacent elements that are equal, replace them with one element with value arr[i] + 1
            arr[i] = arr[i] + 1
            # Remove the next element from the array
            arr.pop(i+1)
            # Decrement the length of the array
            length -= 1
    # Return the minimum length of the array
    return length

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(min_length(arr))

if __name__ == '__main__':
    main()


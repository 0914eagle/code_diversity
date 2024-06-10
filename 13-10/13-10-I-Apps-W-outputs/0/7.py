
def get_min_length(arr):
    # Sort the array in ascending order
    arr.sort()
    # Initialize a variable to keep track of the minimum length
    min_length = len(arr)
    # Loop through the array and check for consecutive duplicates
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            # If there are consecutive duplicates, replace them with a single element with value arr[i] + 1
            arr[i] = arr[i] + 1
            # Remove the next element
            arr.pop(i + 1)
            # Update the minimum length
            min_length -= 1
    return min_length

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_min_length(arr))

if __name__ == '__main__':
    main()


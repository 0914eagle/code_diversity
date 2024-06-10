
def get_min_length(arr):
    # Sort the array in descending order
    arr.sort(reverse=True)
    # Initialize a variable to store the minimum length
    min_length = len(arr)
    # Loop through the array and check if there are any adjacent equal elements
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            # If there are adjacent equal elements, replace them with one element with value arr[i] + 1
            arr[i] += 1
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


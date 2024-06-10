
def get_sorted_array(n, m, arr):
    # Sort the array in ascending order
    arr.sort()
    # Initialize a counter to keep track of the number of digits changed
    count = 0
    # Loop through the array and change the digits as needed
    for i in range(n - 1):
        # If the current element is greater than the next element, change the digits
        if arr[i] > arr[i + 1]:
            # Change the digits of the current element
            arr[i] = arr[i + 1]
            # Change the digits of the next element
            arr[i + 1] = arr[i]
            # Increment the counter
            count += 1
    # Return the sorted array and the number of digits changed
    return arr, count

def main():
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    sorted_arr, count = get_sorted_array(n, m, arr)
    print(*sorted_arr)
    print(count)

if __name__ == '__main__':
    main()


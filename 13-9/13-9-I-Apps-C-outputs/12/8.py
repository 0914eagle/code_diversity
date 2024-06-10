
def get_maximum_sum(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the maximum sum
    max_sum = 0
    # Loop through the array and find the maximum sum
    for i in range(len(arr)):
        max_sum += arr[i]
    return max_sum

def main():
    # Read the input
    n = int(input())
    arr = list(map(int, input().split()))
    # Call the get_maximum_sum function
    max_sum = get_maximum_sum(arr)
    # Print the result
    print(max_sum)

if __name__ == '__main__':
    main()


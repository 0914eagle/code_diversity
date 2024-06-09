
def find_even_subset(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize two variables to keep track of the sum and the current index
    sum, i = 0, 0
    # Loop through the array and check if the sum is even
    while sum % 2 == 0 and i < len(arr):
        # If the sum is even, add the current element to the subset and move to the next element
        sum += arr[i]
        i += 1
    # If the sum is even, return the number of elements in the subset
    if sum % 2 == 0:
        return i
    # If the sum is odd, return -1
    return -1

def main():
    # Read the number of test cases
    t = int(input())
    # Loop through the test cases
    for _ in range(t):
        # Read the length of the array
        n = int(input())
        # Read the array
        arr = list(map(int, input().split()))
        # Find the even subset
        result = find_even_subset(arr)
        # Print the result
        print(result if result != -1 else -1)

if __name__ == '__main__':
    main()



def can_be_reduced_to_one(arr):
    # Sort the array in ascending order
    arr.sort()
    # Initialize a variable to keep track of the number of unique elements
    unique_elements = 1
    # Iterate through the array
    for i in range(len(arr) - 1):
        # Check if the current element is within one unit of the previous element
        if arr[i] - arr[i + 1] <= 1:
            # If they are, merge them into a single element
            arr[i] = arr[i] + arr[i + 1]
            # Delete the next element
            del arr[i + 1]
        else:
            # If they are not, increment the number of unique elements
            unique_elements += 1
    # Check if the number of unique elements is 1
    return unique_elements == 1

def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        n = int(input())
        arr = list(map(int, input().split()))
        if can_be_reduced_to_one(arr):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()


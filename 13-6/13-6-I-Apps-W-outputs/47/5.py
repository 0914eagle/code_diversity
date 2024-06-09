
def get_even_subset(arr):
    # Initialize a set to store the indices of the chosen elements
    chosen_indices = set()
    # Initialize a variable to store the sum of the chosen elements
    chosen_sum = 0
    # Iterate over the array
    for i, num in enumerate(arr):
        # If the number is even, add it to the sum and add its index to the set of chosen indices
        if num % 2 == 0:
            chosen_sum += num
            chosen_indices.add(i)
    # If the sum is even, return the set of chosen indices
    if chosen_sum % 2 == 0:
        return chosen_indices
    # If the sum is odd, return -1
    else:
        return -1

def main():
    # Read the number of test cases
    num_test_cases = int(input())
    # Iterate over the test cases
    for _ in range(num_test_cases):
        # Read the length of the array and the array
        n = int(input())
        arr = list(map(int, input().split()))
        # Get the even subset of the array
        result = get_even_subset(arr)
        # If there is no even subset, print -1
        if result == -1:
            print(-1)
        # Otherwise, print the number of chosen elements and their indices
        else:
            print(len(result))
            print(*result)

if __name__ == '__main__':
    main()


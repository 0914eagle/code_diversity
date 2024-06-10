
def get_minimum_steps(b):
    # Initialize the minimum number of steps to 0
    min_steps = 0
    # Initialize the current sum to 0
    current_sum = 0
    # Iterate through the array b
    for i in range(len(b)):
        # If the current sum is less than the target sum, add the current element to the current sum
        if current_sum < sum(b):
            current_sum += b[i]
            # Increment the minimum number of steps
            min_steps += 1
        # If the current sum is greater than the target sum, subtract the current element from the current sum
        else:
            current_sum -= b[i]
            # Increment the minimum number of steps
            min_steps += 1
    # Return the minimum number of steps
    return min_steps

def main():
    # Read the input n and the array b
    n = int(input())
    b = list(map(int, input().split()))
    # Call the get_minimum_steps function and print the result
    print(get_minimum_steps(b))

if __name__ == '__main__':
    main()


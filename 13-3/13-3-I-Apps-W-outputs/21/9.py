
def get_max_square_side_length(planks):
    # Sort the planks in descending order
    planks.sort(reverse=True)
    # Initialize the maximum side length of the square
    max_side_length = 0
    # Iterate over the planks
    for i in range(len(planks)):
        # Check if the current plank is greater than the maximum side length
        if planks[i] > max_side_length:
            # If so, set the maximum side length to the current plank
            max_side_length = planks[i]
        # Check if the current plank is equal to the maximum side length
        elif planks[i] == max_side_length:
            # If so, we have found a square
            return max_side_length
    # If we reach this point, no square has been found
    return max_side_length


if __name__ == "__main__":
    # Read the number of test cases
    num_test_cases = int(input())
    # Iterate over the test cases
    for i in range(num_test_cases):
        # Read the number of planks
        num_planks = int(input())
        # Read the lengths of the planks
        planks = list(map(int, input().split()))
        # Get the maximum side length of the square
        max_side_length = get_max_square_side_length(planks)
        # Print the maximum side length
        print(max_side_length)


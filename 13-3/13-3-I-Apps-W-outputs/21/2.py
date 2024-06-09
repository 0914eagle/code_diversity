
def get_max_square(planks):
    # Sort the planks in non-decreasing order
    planks.sort()
    # Initialize the maximum side length of the square as 0
    max_side_length = 0
    # Iterate over the planks
    for i in range(len(planks)):
        # Get the length of the current plank
        length = planks[i]
        # Check if the length is greater than the maximum side length
        if length > max_side_length:
            # Iterate over the remaining planks
            for j in range(i+1, len(planks)):
                # Get the length of the current plank
                length2 = planks[j]
                # Check if the length of the current plank is equal to the maximum side length
                if length2 == max_side_length:
                    # Increment the maximum side length by 1
                    max_side_length += 1
                    # Break out of the loop
                    break
    # Return the maximum side length of the square
    return max_side_length

# Main function
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
        max_side_length = get_max_square(planks)
        # Print the maximum side length of the square
        print(max_side_length)


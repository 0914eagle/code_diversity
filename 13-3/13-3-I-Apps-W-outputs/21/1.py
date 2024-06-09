
def get_max_square(planks):
    # Sort the planks in descending order
    planks.sort(reverse=True)
    # Initialize the maximum side length of the square
    max_side_length = 0
    # Iterate over the planks
    for i in range(len(planks)):
        # Check if the current plank is larger than the maximum side length
        if planks[i] > max_side_length:
            # If so, set the maximum side length to the current plank
            max_side_length = planks[i]
        # Check if the current plank is equal to the maximum side length
        elif planks[i] == max_side_length:
            # If so, break the loop
            break
    return max_side_length


if __name__ == "__main__":
    num_test_cases = int(input())
    for i in range(num_test_cases):
        num_planks = int(input())
        planks = list(map(int, input().split()))
        print(get_max_square(planks))


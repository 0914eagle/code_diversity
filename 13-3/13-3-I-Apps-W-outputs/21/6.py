
def get_max_side_length(planks):
    # Sort the planks in descending order
    planks.sort(reverse=True)
    # Initialize the maximum side length as 0
    max_side_length = 0
    # Iterate through the planks
    for i in range(len(planks)):
        # Check if the current plank is greater than the maximum side length
        if planks[i] > max_side_length:
            # If it is, set the maximum side length to the current plank
            max_side_length = planks[i]
    return max_side_length


if __name__ == "__main__":
    num_test_cases = int(input())
    for i in range(num_test_cases):
        num_planks = int(input())
        planks = list(map(int, input().split()))
        print(get_max_side_length(planks))


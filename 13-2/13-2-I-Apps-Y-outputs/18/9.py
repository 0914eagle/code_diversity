
def get_optimal_flavor(n, ls):
    # Sort the list of flavors in ascending order
    sorted_ls = sorted(ls)
    # Initialize the sum of the flavors of the remaining apples
    sum_remaining_apples = sum(sorted_ls[1:])
    # Initialize the sum of the flavors of all apples
    sum_all_apples = sum(sorted_ls)
    # Initialize the minimum absolute difference
    min_abs_diff = abs(sum_all_apples - sum_remaining_apples)
    # Initialize the optimal apple to eat
    optimal_apple = 1
    # Iterate over the list of flavors
    for i in range(1, n):
        # Calculate the sum of the flavors of the remaining apples
        sum_remaining_apples = sum_remaining_apples - sorted_ls[i]
        # Calculate the sum of the flavors of all apples
        sum_all_apples = sum_all_apples - sorted_ls[i]
        # Calculate the absolute difference
        abs_diff = abs(sum_all_apples - sum_remaining_apples)
        # If the absolute difference is smaller than the minimum absolute difference, update the minimum absolute difference and the optimal apple to eat
        if abs_diff < min_abs_diff:
            min_abs_diff = abs_diff
            optimal_apple = i + 1
    # Return the flavor of the apple pie made of the remaining N-1 apples
    return sum_remaining_apples

def main():
    n, ls = map(int, input().split())
    print(get_optimal_flavor(n, ls))

if __name__ == '__main__':
    main()


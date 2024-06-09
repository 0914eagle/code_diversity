
def get_optimal_flavor(n, ls):
    # Sort the list of flavors in ascending order
    sorted_ls = sorted(ls)
    # Initialize the sum of the flavors of the remaining apples
    sum_remaining_apples = sum(sorted_ls[1:])
    # Initialize the sum of the flavors of all apples
    sum_all_apples = sum(sorted_ls)
    # Initialize the minimum difference between the two sums
    min_diff = abs(sum_all_apples - sum_remaining_apples)
    # Initialize the index of the apple to eat
    apple_to_eat = 0
    # Iterate over the list of flavors
    for i in range(1, n):
        # Calculate the sum of the flavors of the remaining apples
        sum_remaining_apples = sum_remaining_apples - sorted_ls[i] + sorted_ls[i-1]
        # Calculate the difference between the two sums
        diff = abs(sum_all_apples - sum_remaining_apples)
        # If the difference is smaller than the minimum difference, update the minimum difference and the index of the apple to eat
        if diff < min_diff:
            min_diff = diff
            apple_to_eat = i
    # Return the flavor of the apple pie made of the remaining N-1 apples
    return sum_remaining_apples

def main():
    n, ls = map(int, input().split())
    print(get_optimal_flavor(n, ls))

if __name__ == '__main__':
    main()


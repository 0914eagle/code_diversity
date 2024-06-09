
def find_min_diff(k, n):
    # Convert the integer n to a list of individual digits
    n_list = [int(digit) for digit in str(n)]
    # Initialize a variable to keep track of the minimum number of digits that differ
    min_diff = len(n_list)
    # Iterate over all possible digits that could be changed in the initial number
    for i in range(10):
        # If the current digit is not in the list of individual digits of n, continue to the next iteration
        if i not in n_list:
            continue
        # Find the index of the current digit in the list of individual digits of n
        index = n_list.index(i)
        # Replace the current digit with a different digit in the list of individual digits of n
        n_list[index] = (i + 1) % 10
        # Calculate the sum of the digits in the modified list of individual digits of n
        modified_sum = sum(n_list)
        # If the sum of the digits in the modified list of individual digits of n is less than k, update the minimum number of digits that differ
        if modified_sum < k:
            min_diff = min(min_diff, index + 1)
    # Return the minimum number of digits that differ between the initial number and n
    return min_diff


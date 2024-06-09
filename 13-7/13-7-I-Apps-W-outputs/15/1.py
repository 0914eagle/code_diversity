
def solve(k, n):
    # Initialize a variable to store the minimum number of digits
    min_digits = 0
    # Convert the input numbers to strings
    k_str = str(k)
    n_str = str(n)
    # Loop through each digit in the input numbers
    for i in range(len(k_str)):
        # If the digits are not equal, increment the minimum number of digits
        if k_str[i] != n_str[i]:
            min_digits += 1
    # Return the minimum number of digits
    return min_digits


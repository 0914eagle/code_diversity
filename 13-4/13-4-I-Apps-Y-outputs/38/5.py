
def solve(a, f):
    # Convert the input string to a list of integers
    a = [int(x) for x in a]
    # Initialize the maximum number to be the original number
    max_num = a[:]
    # Iterate over the digits of the number
    for i in range(len(a)):
        # If the current digit is not equal to the function value, update the maximum number
        if a[i] != f[a[i] - 1]:
            max_num[i] = f[a[i] - 1]
    # Return the maximum number
    return max_num



def solve(l, n):
    # Initialize the number of layers as 1
    k = 1
    # Loop until the number of layers is greater than or equal to the given input
    while k < l // n:
        # Increment the number of layers by 1
        k += 1
    # Return the smallest number of layers that will prevent crises from happening
    return k


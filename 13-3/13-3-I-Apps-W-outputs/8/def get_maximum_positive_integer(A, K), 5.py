
def get_maximum_positive_integer(A, K):
    # Initialize the maximum positive integer as 1
    max_positive_integer = 1
    # Loop through each element in A
    for i in range(len(A)):
        # Find the greatest common divisor (GCD) of the current element and the maximum positive integer
        gcd = get_gcd(A[i], max_positive_integer)
        # If the GCD is not 1, it means that the maximum positive integer does not divide the current element
        if gcd != 1:
            # Update the maximum positive integer to be the GCD
            max_positive_integer = gcd
            # If the maximum positive integer is greater than the number of remaining operations, return -1
            if max_positive_integer > K:
                return -1
    # If all elements in A are divisible by the maximum positive integer, return it
    return max_positive_integer

def get_gcd(a, b):
    # Base case: if b is 0, the GCD is a
    if b == 0:
        return a
    # Recursive case: calculate the GCD of b and the remainder of a divided by b
    else:
        return get_gcd(b, a % b)

# Test the function with the sample input
A = [8, 20]
K = 3
print(get_maximum_positive_integer(A, K))


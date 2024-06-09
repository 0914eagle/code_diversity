
def get_max_divisor(A, K):
    # Initialize the maximum divisor as 1
    max_divisor = 1
    # Loop through each element in A
    for i in range(len(A)):
        # Find the greatest common divisor (GCD) of the current element and the maximum divisor
        gcd = gcd_of_two(A[i], max_divisor)
        # Update the maximum divisor as the larger of the current element and the GCD
        max_divisor = max(A[i], gcd)
    # If K is greater than 0, we can perform the operations
    if K > 0:
        # Loop through each operation
        for _ in range(K):
            # Find the maximum divisor that divides all elements in A
            max_divisor = get_max_divisor_helper(A, max_divisor)
    # Return the maximum divisor
    return max_divisor

def get_max_divisor_helper(A, max_divisor):
    # Initialize the maximum divisor as 1
    max_divisor = 1
    # Loop through each element in A
    for i in range(len(A)):
        # Find the greatest common divisor (GCD) of the current element and the maximum divisor
        gcd = gcd_of_two(A[i], max_divisor)
        # Update the maximum divisor as the larger of the current element and the GCD
        max_divisor = max(A[i], gcd)
    # Return the maximum divisor
    return max_divisor

def gcd_of_two(a, b):
    # Base case: if b is 0, the GCD is a
    if b == 0:
        return a
    # Recursive case: divide the larger number by the smaller number and recur
    elif a > b:
        return gcd_of_two(b, a % b)
    else:
        return gcd_of_two(a, b % a)


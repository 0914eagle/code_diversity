
def get_maximum_divisor(A, K):
    # Initialize the maximum divisor as 1
    max_divisor = 1
    # Loop through each element in A
    for i in range(len(A)):
        # Find the greatest common divisor (GCD) of the current element and the maximum divisor
        gcd = gcd_of_two(A[i], max_divisor)
        # Update the maximum divisor as the larger of the two
        max_divisor = max(gcd, max_divisor)
    # Loop through each operation
    for _ in range(K):
        # Find the maximum element in A
        max_element = max(A)
        # Find the index of the maximum element
        max_index = A.index(max_element)
        # Update the maximum divisor as the larger of the two
        max_divisor = max(max_divisor, max_element)
        # Update the element at the maximum index as the maximum divisor
        A[max_index] = max_divisor
    # Return the maximum divisor
    return max_divisor

def gcd_of_two(a, b):
    # Base case: if b is 0, return a
    if b == 0:
        return a
    # Recursive case: calculate the GCD of b and the remainder of a divided by b
    else:
        return gcd_of_two(b, a % b)


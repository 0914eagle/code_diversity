
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
        # Find the two elements that are not equal and have the largest difference
        i, j = get_largest_difference(A)
        # Update the elements of A as described in the problem statement
        A[i] += 1
        A[j] -= 1
        # Find the new GCD of the updated elements
        gcd = gcd_of_two(A[i], A[j])
        # Update the maximum divisor as the larger of the two
        max_divisor = max(gcd, max_divisor)
    return max_divisor

def gcd_of_two(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def get_largest_difference(A):
    max_diff = 0
    i = 0
    j = 1
    for k in range(len(A)):
        for l in range(k+1, len(A)):
            diff = abs(A[k] - A[l])
            if diff > max_diff:
                max_diff = diff
                i = k
                j = l
    return i, j

A = [8, 20]
K = 3
print(get_maximum_divisor(A, K))


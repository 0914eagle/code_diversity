
def solve(N, K, A):
    # Initialize the maximum possible positive integer that divides every element of A
    max_divisor = 1

    # Loop through each operation
    for i in range(K):
        # Find the greatest common divisor of all elements in A
        gcd = find_gcd(A)

        # Update the maximum possible positive integer that divides every element of A
        max_divisor = max(max_divisor, gcd)

        # Update A by adding 1 to the ith element and subtracting 1 from the jth element
        i, j = find_indices_to_update(A)
        A[i] += 1
        A[j] -= 1

    return max_divisor

def find_gcd(A):
    return reduce(gcd, A)

def find_indices_to_update(A):
    # Find the indices of the two elements with the largest absolute difference
    i, j = 0, 1
    max_diff = abs(A[0] - A[1])
    for k in range(2, len(A)):
        diff = abs(A[k] - A[k-1])
        if diff > max_diff:
            i, j = k-1, k
            max_diff = diff

    return i, j


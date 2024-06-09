
def restore_permutation(n, q):
    # Initialize a list to store the permutation
    permutation = [0] * n
    # Set the first element of the permutation to 1
    permutation[0] = 1
    # Iterate over the remaining elements of the permutation
    for i in range(1, n):
        # Find the next element of the permutation based on the previous elements and the given array q
        permutation[i] = permutation[i-1] + q[i-1]
        # If the element is already used, return -1
        if permutation[i] in permutation[:i]:
            return -1
    # Return the permutation if it is valid
    return permutation

if __name__ == '__main__':
    n = int(input())
    q = list(map(int, input().split()))
    print(*restore_permutation(n, q))



def solve(N, A, B):
    # Initialize a list to store the permutation
    perm = list(range(1, N+1))
    # Loop through each element in the permutation
    for i in range(N):
        # If the element is equal to A or B, skip it
        if perm[i] in [A, B]:
            continue
        # If the element is not equal to A or B, find the minimum positive integer j such that f(i, j) = i
        j = 1
        while True:
            if f(perm[i], j) == perm[i]:
                break
            j += 1
        # Swap the element with the element at index j in the permutation
        perm[i], perm[j-1] = perm[j-1], perm[i]
    # If the permutation is valid, return it, otherwise return -1
    if valid_permutation(perm, A, B):
        return perm
    else:
        return -1

# Function to check if a permutation is valid
def valid_permutation(perm, A, B):
    # Loop through each element in the permutation
    for i in range(len(perm)):
        # If the element is equal to A or B, skip it
        if perm[i] in [A, B]:
            continue
        # If the element is not equal to A or B, find the minimum positive integer j such that f(i, j) = i
        j = 1
        while True:
            if f(perm[i], j) == perm[i]:
                break
            j += 1
        # If the element is not equal to A or B and the minimum positive integer j such that f(i, j) = i is not equal to A or B, the permutation is invalid
        if perm[i] != A and perm[i] != B and perm[j-1] != A and perm[j-1] != B:
            return False
    # If all elements in the permutation are valid, the permutation is valid
    return True

# Function to calculate f(i, j)
def f(i, j):
    if j == 1:
        return i
    else:
        return f(perm[i], j-1)

perm = solve(9, 2, 5)
print(perm)


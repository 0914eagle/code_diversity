
def get_permutation(n, q):
    # Initialize a list to store the permutation
    permutation = [0] * n
    # Set the first element of the permutation to 1
    permutation[0] = 1
    # Iterate over the remaining elements of the permutation
    for i in range(1, n):
        # Find the next element of the permutation using the formula p_i = q_i + p_{i-1}
        permutation[i] = q[i-1] + permutation[i-1]
    # Return the permutation
    return permutation

def main():
    # Read the input n and q
    n, q = map(int, input().split())
    # Call the get_permutation function to get the permutation
    permutation = get_permutation(n, q)
    # Print the permutation
    print(*permutation)

if __name__ == '__main__':
    main()


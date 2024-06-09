
def solve(N, molecule):
    # Initialize variables
    count = 0
    K = 1

    # Loop through the molecule and count the number of mutations needed
    for i in range(N):
        if molecule[i] == 'A':
            count += 1
        elif molecule[i] == 'B':
            count += 2
        K = max(K, count)

    # Return the minimum number of mutations needed
    return K


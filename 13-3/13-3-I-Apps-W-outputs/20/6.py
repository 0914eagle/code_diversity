
def solve(X, Y, Z, K, A, B, C):
    # Calculate the deliciousness of each cake
    cakes = []
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                cakes.append((A[i] + B[j] + C[k], i, j, k))

    # Sort the cakes in descending order of deliciousness
    cakes.sort(reverse=True)

    # Return the deliciousness of the first K cakes
    return [cake[0] for cake in cakes[:K]]


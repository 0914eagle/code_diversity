
def solve(X, Y, Z, K, A, B, C):
    # Calculate the deliciousness of each cake
    cakes = []
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                cakes.append([A[i], B[j], C[k]])

    # Sort the cakes in descending order of their deliciousness
    cakes.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)

    # Return the desired number of cakes
    return [cakes[i][0] + cakes[i][1] + cakes[i][2] for i in range(K)]


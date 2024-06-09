
def solve(X, Y, Z, K, A, B, C):
    # Calculate the deliciousness of each combination of cakes
    deliciousness = []
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                deliciousness.append(A[i] + B[j] + C[k])
    
    # Sort the deliciousness in descending order
    deliciousness.sort(reverse=True)
    
    # Return the first K values
    return deliciousness[:K]


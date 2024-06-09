
def solve(X, Y, Z, K, A, B, C):
    # Calculate the deliciousness of each combination of cakes
    combinations = []
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                combinations.append(A[i] + B[j] + C[k])
    
    # Sort the combinations in descending order
    combinations.sort(reverse=True)
    
    # Return the first K combinations
    return combinations[:K]



def solve(X, Y, Z, K, A, B, C):
    # Calculate the total number of ways to choose three cakes
    total_ways = X * Y * Z
    
    # Create a list to store the deliciousness of each cake
    cake_list = []
    
    # Add the deliciousness of the cakes with 1-shaped candles to the list
    for i in range(X):
        cake_list.append(A[i])
    
    # Add the deliciousness of the cakes with 2-shaped candles to the list
    for i in range(Y):
        cake_list.append(B[i])
    
    # Add the deliciousness of the cakes with 3-shaped candles to the list
    for i in range(Z):
        cake_list.append(C[i])
    
    # Sort the list in descending order
    cake_list.sort(reverse=True)
    
    # Return the first K elements of the list
    return cake_list[:K]



def solve(X):
    # Initialize variables
    k = 0
    Y = []
    
    # Loop through possible values of k
    for i in range(1, 10):
        # Calculate the product of the first i factors
        product = 1
        for j in range(1, i+1):
            product *= j
            
        # If the product is equal to X, add the factor to the list and break the loop
        if product == X:
            Y.append(i)
            break
    
    # Return the number of factors
    return len(Y)


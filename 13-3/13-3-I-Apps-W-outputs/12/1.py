
def f1(K):
    # Calculate the number of initial configurations that lead to the final
    num_configurations = 1
    for i in range(K):
        num_configurations *= 2 * K - i
    
    return num_configurations % (10**9 + 9)


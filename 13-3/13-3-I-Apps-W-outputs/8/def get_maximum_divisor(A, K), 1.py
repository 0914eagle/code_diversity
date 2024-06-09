
def get_maximum_divisor(A, K):
    # Initialize the maximum divisor as 1
    max_divisor = 1
    
    # Loop through each element in A
    for i in range(len(A)):
        # Find the greatest common divisor (GCD) of the current element and the maximum divisor
        gcd = gcd_of_two(A[i], max_divisor)
        
        # If the GCD is 1, then the current element is already divisible by the maximum divisor
        if gcd == 1:
            continue
        
        # Otherwise, update the maximum divisor to be the GCD
        max_divisor = gcd
    
    # If K is 0, then we can return the maximum divisor immediately
    if K == 0:
        return max_divisor
    
    # Otherwise, we need to perform the operations
    for i in range(K):
        # Find the two elements in A that have the smallest GCD with the maximum divisor
        gcd_values = []
        for j in range(len(A)):
            gcd_values.append(gcd_of_two(A[j], max_divisor))
        min_gcd_index = gcd_values.index(min(gcd_values))
        
        # Update the maximum divisor to be the GCD of the two elements
        max_divisor = gcd_of_two(A[min_gcd_index], A[(min_gcd_index + 1) % len(A)])
    
    return max_divisor

def gcd_of_two(a, b):
    if b == 0:
        return a
    else:
        return gcd_of_two(b, a % b)

# Test the function with the sample input
A = [8, 20]
K = 3
print(get_maximum_divisor(A, K))



def solve(A, K, Q):
    # Step 1: Sort the input array
    A.sort()
    
    # Step 2: Initialize the smallest and largest values
    smallest, largest = A[0], A[0]
    
    # Step 3: Loop through the input array and find the smallest and largest values
    for i in range(1, len(A)):
        if A[i] < smallest:
            smallest = A[i]
        if A[i] > largest:
            largest = A[i]
    
    # Step 4: Return the difference between the smallest and largest values
    return largest - smallest


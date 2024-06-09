
def solve(a, b, x):
    # Calculate the dot product of a and b to get the matrix c
    c = [[a[i] * b[j] for j in range(len(b))] for i in range(len(a))]
    
    # Initialize the maximum area to 0
    max_area = 0
    
    # Iterate over each possible starting point (i, j)
    for i in range(len(a)):
        for j in range(len(b)):
            # Initialize the current area to 0
            current_area = 0
            
            # Iterate over each possible ending point (k, l)
            for k in range(i, len(a)):
                for l in range(j, len(b)):
                    # Calculate the current area
                    current_area += c[k][l]
                    
                    # If the current area is less than or equal to x, update the maximum area
                    if current_area <= x:
                        max_area = max(max_area, (k - i + 1) * (l - j + 1))
    
    # Return the maximum area
    return max_area


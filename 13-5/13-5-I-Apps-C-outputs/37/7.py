
def solve(a, b, x):
    # Calculate the dot product of a and b to get the matrix c
    c = [[a[i] * b[j] for j in range(len(b))] for i in range(len(a))]
    
    # Initialize the maximum area to 0
    max_area = 0
    
    # Iterate over each possible starting point (x1, y1)
    for x1 in range(len(a)):
        for y1 in range(len(b)):
            # Initialize the current sum to 0
            current_sum = 0
            
            # Iterate over each possible ending point (x2, y2)
            for x2 in range(x1, len(a)):
                for y2 in range(y1, len(b)):
                    # Calculate the current sum
                    current_sum += sum(c[x2][y1:y2+1])
                    
                    # If the current sum is less than or equal to x, update the maximum area
                    if current_sum <= x:
                        max_area = max(max_area, (x2-x1+1) * (y2-y1+1))
    
    # Return the maximum area
    return max_area


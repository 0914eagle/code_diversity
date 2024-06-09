
def solve(a, b, x):
    # Calculate the dot product of a and b to get the matrix c
    c = [[a[i] * b[j] for j in range(len(b))] for i in range(len(a))]
    
    # Initialize the maximum area and the corresponding indices
    max_area = 0
    x1, x2, y1, y2 = 0, 0, 0, 0
    
    # Iterate through all possible pairs of indices
    for i in range(len(a)):
        for j in range(len(b)):
            # Calculate the area of the current subrectangle
            area = (i - x1 + 1) * (j - y1 + 1)
            
            # If the area is greater than the maximum area, update the maximum area and the corresponding indices
            if area > max_area and sum(sum(c[x1:i+1], [])) <= x:
                max_area = area
                x2, y2 = i, j
    
    # Return the maximum area
    return max_area


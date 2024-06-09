
def solve(a, b):
    # Find the closest integer value of x such that (x, x) lies on the line
    x = int((a * 1.0) / b)
    
    # Check if the point (x, x) lies on the line
    if a % b == 0:
        return x
    
    # If the point does not lie on the line, then there is no solution
    return -1


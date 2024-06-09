
def get_diagonal_intersections(N):
    # Calculate the number of diagonals
    num_diagonals = N * (N - 3) // 2
    
    # Initialize a list to store the intersections
    intersections = []
    
    # Iterate over each diagonal
    for i in range(num_diagonals):
        # Find the endpoints of the diagonal
        x1, y1 = get_endpoint(i, N)
        x2, y2 = get_endpoint(i + 1, N)
        
        # Check if the diagonal intersects with any other diagonal
        for j in range(i + 2, num_diagonals):
            x3, y3 = get_endpoint(j, N)
            x4, y4 = get_endpoint(j + 1, N)
            
            # Check if the diagonals intersect
            if do_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
                # If they do, add the intersection to the list
                intersections.append((i, j))
    
    # Return the number of intersections
    return len(intersections)

def get_endpoint(i, N):
    # Find the endpoint of the diagonal
    x = i % N
    y = (i // N) + 1
    return x, y

def do_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    # Check if the lines intersect
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return False
    
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denom
    return 0 <= t <= 1 and 0 <= u <= 1

def main():
    N = int(input())
    print(get_diagonal_intersections(N))

if __name__ == '__main__':
    main()


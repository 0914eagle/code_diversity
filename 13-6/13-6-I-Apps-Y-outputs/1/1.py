
def get_intersections(N):
    # Calculate the number of diagonals
    num_diagonals = N * (N - 3) // 2
    
    # Initialize a list to store the intersections
    intersections = []
    
    # Iterate over each diagonal
    for i in range(num_diagonals):
        # Find the endpoints of the diagonal
        endpoint1 = i
        endpoint2 = (i + 1) % N
        
        # Check if the diagonal intersects with any other diagonal
        for j in range(num_diagonals):
            if i == j:
                continue
            else:
                # Find the endpoints of the other diagonal
                other_endpoint1 = j
                other_endpoint2 = (j + 1) % N
                
                # Check if the diagonals intersect
                if endpoint1 == other_endpoint2 or endpoint2 == other_endpoint1:
                    # If the diagonals intersect, add the intersection to the list
                    intersections.append((endpoint1, endpoint2))
    
    # Return the number of intersections
    return len(set(intersections))

def main():
    N = int(input())
    print(get_intersections(N))

if __name__ == '__main__':
    main()


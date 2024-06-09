
import math

def get_intersections(N):
    # Calculate the number of diagonals
    num_diagonals = N * (N - 3) // 2
    
    # Initialize an array to store the intersections
    intersections = [0] * num_diagonals
    
    # Iterate through each diagonal
    for i in range(num_diagonals):
        # Calculate the index of the first vertex
        v1 = i // (N - 1)
        
        # Calculate the index of the second vertex
        v2 = (v1 + 1) % N
        
        # Iterate through each diagonal that is not parallel to the current diagonal
        for j in range(num_diagonals):
            # Calculate the index of the first vertex of the second diagonal
            w1 = j // (N - 1)
            
            # Calculate the index of the second vertex of the second diagonal
            w2 = (w1 + 1) % N
            
            # Check if the two diagonals intersect
            if v1 != w1 and v1 != w2 and v2 != w1 and v2 != w2:
                # Calculate the slope of the first diagonal
                m1 = (N - 1 - v1 + v2) / (w1 - v1)
                
                # Calculate the slope of the second diagonal
                m2 = (N - 1 - w1 + w2) / (v1 - w1)
                
                # Check if the slopes are equal
                if m1 == m2:
                    # Increment the number of intersections
                    intersections[i] += 1
    
    # Return the number of intersections
    return sum(intersections)

def main():
    # Read the number of vertices
    N = int(input())
    
    # Calculate the number of intersections
    num_intersections = get_intersections(N)
    
    # Print the number of intersections
    print(num_intersections)

if __name__ == '__main__':
    main()


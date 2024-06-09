
import sys

# Function to count the number of ways to make the figure complete
def count_ways(N, holes):
    # Initialize the number of ways to 1
    ways = 1
    
    # Iterate over each part
    for i in range(N):
        # Get the number of holes in the current part
        num_holes = holes[i]
        
        # Iterate over each hole in the current part
        for j in range(num_holes):
            # Increment the number of ways by the number of ways to connect the current hole
            ways += count_ways_helper(i, j, N, holes)
    
    # Return the number of ways
    return ways % 998244353

# Helper function to count the number of ways to connect a hole
def count_ways_helper(part, hole, N, holes):
    # Initialize the number of ways to 0
    ways = 0
    
    # Iterate over each part
    for i in range(N):
        # Check if the current part is not the same as the part with the hole
        if i != part:
            # Get the number of holes in the current part
            num_holes = holes[i]
            
            # Iterate over each hole in the current part
            for j in range(num_holes):
                # Check if the current hole is not the same as the hole in the current part
                if j != hole:
                    # Increment the number of ways by 1
                    ways += 1
    
    # Return the number of ways
    return ways

# Main function
if __name__ == "__main__":
    # Read the input from stdin
    input_list = sys.stdin.read().split()
    
    # Get the number of parts and holes
    N = int(input_list[0])
    holes = list(map(int, input_list[1:]))
    
    # Call the count_ways function to count the number of ways to make the figure complete
    ways = count_ways(N, holes)
    
    # Print the number of ways
    print(ways)


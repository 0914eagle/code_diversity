
def get_starting_circles(circle, k):
    # Initialize a set to store the distinct starting circles
    starting_circles = set()
    
    # Loop through each possible starting circle
    for i in range(len(circle)):
        # Get the starting circle by rotating the input circle by i positions
        starting_circle = circle[i:] + circle[:i]
        
        # Check if the starting circle is the same as the input circle after k transformations
        if starting_circle == get_transformed_circle(starting_circle, k):
            # If it is, add it to the set of distinct starting circles
            starting_circles.add(starting_circle)
    
    # Return the number of distinct starting circles
    return len(starting_circles)

def get_transformed_circle(circle, k):
    # Initialize a list to store the transformed circle
    transformed_circle = []
    
    # Loop through each position in the circle
    for i in range(len(circle)):
        # Get the current position in the circle
        current_position = i % len(circle)
        
        # Get the color of the current position in the circle
        current_color = circle[current_position]
        
        # Get the next position in the circle
        next_position = (current_position + 1) % len(circle)
        
        # Get the color of the next position in the circle
        next_color = circle[next_position]
        
        # Check if the current position and the next position have the same color
        if current_color == next_color:
            # If they do, add a black pebble to the transformed circle
            transformed_circle.append("B")
        else:
            # If they don't, add a white pebble to the transformed circle
            transformed_circle.append("W")
    
    # Return the transformed circle
    return transformed_circle

if __name__ == '__main__':
    # Read the input from stdin
    n, k = input().split()
    circle = input()
    
    # Call the function to get the number of distinct starting circles
    result = get_starting_circles(circle, k)
    
    # Print the result to stdout
    print(result)


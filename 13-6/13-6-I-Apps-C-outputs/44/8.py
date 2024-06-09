
def get_starting_circles(circle, k):
    # Initialize a set to store the starting circles
    starting_circles = set()
    
    # Iterate over the possible starting circles
    for i in range(len(circle)):
        # Create a copy of the original circle
        current_circle = circle[:]
        
        # Iterate over the possible transformations
        for j in range(k):
            # Get the current color of the first pebble
            current_color = current_circle[i]
            
            # Get the next color of the pebble
            next_color = "B" if current_color == "W" else "W"
            
            # Insert the next color of the pebble
            current_circle.insert(i, next_color)
            
            # Remove the last pebble
            current_circle.pop()
            
        # Add the current circle to the set of starting circles
        starting_circles.add(tuple(current_circle))
    
    # Return the number of distinct starting circles
    return len(starting_circles)

def main():
    # Read the input
    n, k = map(int, input().split())
    circle = input()
    
    # Call the function to get the number of distinct starting circles
    result = get_starting_circles(circle, k)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()


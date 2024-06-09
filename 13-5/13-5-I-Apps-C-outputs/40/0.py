
def get_starting_circles(circle, k):
    # Initialize a set to store the starting circles
    starting_circles = set()
    
    # Iterate over the possible starting circles
    for i in range(len(circle)):
        # Create a copy of the circle and rotate it by i positions
        rotated_circle = circle[i:] + circle[:i]
        
        # Check if the rotated circle is the same as the original circle after k transformations
        if rotated_circle == circle:
            # Add the starting circle to the set
            starting_circles.add(rotated_circle)
    
    # Return the number of distinct starting circles
    return len(starting_circles)

def main():
    # Read the input from stdin
    n, k = map(int, input().split())
    circle = input()
    
    # Call the function to get the number of distinct starting circles
    result = get_starting_circles(circle, k)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()


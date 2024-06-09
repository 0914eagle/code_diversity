
def get_starting_circles(circle, k):
    # Initialize a set to store the distinct starting circles
    starting_circles = set()
    
    # Iterate over the possible starting circles
    for i in range(len(circle)):
        # Get the starting circle by rotating the input circle by i positions
        starting_circle = circle[i:] + circle[:i]
        
        # Add the starting circle to the set of distinct starting circles
        starting_circles.add(starting_circle)
    
    # Return the number of distinct starting circles
    return len(starting_circles)

def main():
    # Read the input from stdin
    n, k = map(int, input().split())
    circle = input()
    
    # Call the function to get the number of distinct starting circles
    result = get_starting_circles(circle, k)
    
    # Print the result to stdout
    print(result)

if __name__ == '__main__':
    main()


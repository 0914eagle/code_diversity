
def get_starting_circles(circle, k):
    # Initialize a set to store the starting circles
    starting_circles = set()
    
    # Loop through each possible starting circle
    for i in range(len(circle)):
        # Get the starting circle by rotating the input circle i positions
        starting_circle = circle[i:] + circle[:i]
        
        # Add the starting circle to the set if it is not already present
        if starting_circle not in starting_circles:
            starting_circles.add(starting_circle)
    
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


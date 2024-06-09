
def get_distinct_starting_circles(circle, k):
    # Initialize a set to store the distinct starting circles
    distinct_circles = set()
    
    # Loop through each possible starting circle
    for i in range(len(circle)):
        # Get the current circle by rotating the original circle i positions
        current_circle = circle[i:] + circle[:i]
        
        # Loop through each possible transformation
        for j in range(k):
            # Get the next circle by inserting a black pebble between two neighboring pebbles of the same color, and a white pebble between two neighboring pebbles of different colors
            next_circle = ""
            for i in range(len(current_circle) - 1):
                if current_circle[i] == current_circle[i + 1]:
                    next_circle += "B"
                else:
                    next_circle += "W"
            next_circle += current_circle[-1]
            
            # Add the current circle to the set of distinct starting circles
            distinct_circles.add(next_circle)
    
    # Return the number of distinct starting circles
    return len(distinct_circles)

def main():
    # Read the input
    n, k = map(int, input().split())
    circle = input()
    
    # Call the function to get the number of distinct starting circles
    result = get_distinct_starting_circles(circle, k)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()


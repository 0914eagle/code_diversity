
def get_max_groups(n, m):
    # Initialize a list to store the positions of the cats that have left
    left_cats = []
    
    # Loop through the number of cats that have left
    for i in range(m):
        # Get a random position of a cat that has left
        pos = random.randint(0, n-1)
        
        # Add the position to the list of left cats
        left_cats.append(pos)
    
    # Sort the list of left cats in ascending order
    left_cats.sort()
    
    # Initialize a variable to store the maximum number of groups
    max_groups = 1
    
    # Loop through the list of left cats
    for i in range(len(left_cats)):
        # Check if the current position is not the last position in the list
        if i != len(left_cats) - 1:
            # Calculate the distance between the current position and the next position
            dist = left_cats[i+1] - left_cats[i]
            
            # Check if the distance is greater than 1
            if dist > 1:
                # Increment the maximum number of groups
                max_groups += 1
    
    # Return the maximum number of groups
    return max_groups

def main():
    # Read the input from stdin
    n, m = map(int, input().split())
    
    # Call the get_max_groups function and store the result
    result = get_max_groups(n, m)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()


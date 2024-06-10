
def get_min_max_occupied_houses(n, x):
    # Initialize the minimum and maximum number of occupied houses
    min_occupied_houses = 0
    max_occupied_houses = 0
    
    # Iterate over all possible moves for each friend
    for i in range(n):
        # Get the current and next positions of the friend
        current_position = x[i]
        next_position = current_position + 1
        
        # Check if the next position is valid
        if next_position <= n:
            # Increment the minimum number of occupied houses
            min_occupied_houses += 1
            
            # Check if the next position is already occupied
            if next_position in x:
                # Increment the maximum number of occupied houses
                max_occupied_houses += 1
    
    # Return the minimum and maximum number of occupied houses
    return min_occupied_houses, max_occupied_houses

def main():
    # Read the input
    n = int(input())
    x = list(map(int, input().split()))
    
    # Call the function to get the minimum and maximum number of occupied houses
    min_occupied_houses, max_occupied_houses = get_min_max_occupied_houses(n, x)
    
    # Print the minimum and maximum number of occupied houses
    print(min_occupied_houses, max_occupied_houses)

if __name__ == '__main__':
    main()



def get_min_max_occupied_houses(n, x):
    # Initialize the minimum and maximum number of occupied houses
    min_occupied_houses = 0
    max_occupied_houses = 0
    
    # Iterate over all possible moves for each friend
    for i in range(n):
        # Get the current and next positions of the friend
        current_position = x[i]
        next_position = current_position + 1
        
        # If the friend can move to the next position, update the minimum and maximum number of occupied houses
        if next_position <= n:
            min_occupied_houses += 1
            max_occupied_houses += 1
        
        # If the friend can move to the previous position, update the minimum and maximum number of occupied houses
        previous_position = current_position - 1
        if previous_position >= 0:
            min_occupied_houses += 1
            max_occupied_houses += 1
    
    # Return the minimum and maximum number of occupied houses
    return min_occupied_houses, max_occupied_houses

def main():
    # Read the number of friends and their initial positions
    n = int(input())
    x = list(map(int, input().split()))
    
    # Get the minimum and maximum number of occupied houses
    min_occupied_houses, max_occupied_houses = get_min_max_occupied_houses(n, x)
    
    # Print the minimum and maximum number of occupied houses
    print(min_occupied_houses, max_occupied_houses)

if __name__ == '__main__':
    main()


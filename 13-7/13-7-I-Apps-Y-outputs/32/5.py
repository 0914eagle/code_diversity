
def get_min_max_occupied_houses(n, x):
    # Initialize the minimum and maximum number of occupied houses
    min_occupied_houses = 0
    max_occupied_houses = 0
    
    # Iterate over all possible moves
    for i in range(n):
        # Get the current and next positions of the i-th friend
        current_position = x[i]
        next_position = x[i] + 1 if x[i] < n else 0
        
        # Update the minimum and maximum number of occupied houses
        min_occupied_houses = max(min_occupied_houses, current_position, next_position)
        max_occupied_houses = max(max_occupied_houses, current_position, next_position, n+1)
    
    # Return the minimum and maximum number of occupied houses
    return min_occupied_houses, max_occupied_houses

def main():
    # Read the input
    n = int(input())
    x = list(map(int, input().split()))
    
    # Get the minimum and maximum number of occupied houses
    min_occupied_houses, max_occupied_houses = get_min_max_occupied_houses(n, x)
    
    # Print the minimum and maximum number of occupied houses
    print(min_occupied_houses, max_occupied_houses)

if __name__ == '__main__':
    main()


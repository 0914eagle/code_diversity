
def get_min_max_occupied_houses(n, x):
    # Initialize the minimum and maximum number of occupied houses
    min_occupied_houses = 0
    max_occupied_houses = 0
    
    # Iterate over each friend and their possible moves
    for i in range(n):
        # Check if the friend can move to the left
        if x[i] > 1:
            min_occupied_houses += 1
            max_occupied_houses += 1
        
        # Check if the friend can move to the right
        if x[i] < n:
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


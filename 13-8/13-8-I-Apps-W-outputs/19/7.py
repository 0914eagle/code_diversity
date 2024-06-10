
def get_min_operations(colors):
    # Initialize variables
    n = len(colors)
    min_operations = 0
    i = 0
    
    # Loop through the colors
    while i < n:
        # Check if the current color is the same as the next color
        if colors[i] == colors[i+1]:
            # If they are the same, increment i by 2
            i += 2
        else:
            # If they are not the same, increment min_operations by 1
            min_operations += 1
            # And increment i by 1
            i += 1
    
    return min_operations

def main():
    # Read the number of marbles and the colors of the marbles
    n = int(input())
    colors = list(map(int, input().split()))
    
    # Call the get_min_operations function and print the result
    print(get_min_operations(colors))

if __name__ == '__main__':
    main()



def get_min_operations(stones):
    # Initialize the minimum number of operations to 0
    min_operations = 0
    
    # Loop through the stones and check if there is a white stone next to a red stone
    for i in range(len(stones) - 1):
        if stones[i] == "W" and stones[i + 1] == "R":
            # If there is, increment the minimum number of operations
            min_operations += 1
    
    # Return the minimum number of operations
    return min_operations

def main():
    # Read the number of stones and the colors of the stones from stdin
    num_stones = int(input())
    stones = input()
    
    # Call the get_min_operations function and print the result
    print(get_min_operations(stones))

if __name__ == "__main__":
    main()


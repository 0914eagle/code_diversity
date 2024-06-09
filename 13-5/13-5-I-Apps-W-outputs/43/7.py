
def get_min_operations(stones):
    # Initialize the number of operations to 0
    operations = 0
    
    # Loop through the stones and check if there is a white stone next to a red stone
    for i in range(len(stones) - 1):
        if stones[i] == "W" and stones[i + 1] == "R":
            # If there is, increase the number of operations by 1
            operations += 1
    
    # Return the number of operations needed to reach a situation without a white stone next to a red stone
    return operations

def main():
    # Read the number of stones and the colors of the stones from stdin
    n = int(input())
    stones = list(input())
    
    # Call the get_min_operations function and print the result
    print(get_min_operations(stones))

if __name__ == '__main__':
    main()


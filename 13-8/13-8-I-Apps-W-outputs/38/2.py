
def get_number_of_ways(a, b, c):
    # Initialize the number of ways to build bridges
    number_of_ways = 1
    
    # Loop through each cluster of islands
    for cluster in [a, b, c]:
        # Get the number of islands in the current cluster
        num_islands = cluster
        
        # Loop through each island in the current cluster
        for i in range(num_islands):
            # Get the number of bridges that can be built from the current island
            num_bridges = num_islands - i - 1
            
            # Loop through each bridge that can be built from the current island
            for j in range(num_bridges):
                # Get the number of ways to build the current bridge
                num_ways = number_of_ways
                
                # Loop through each island that is not the current island
                for k in range(i + 1, num_islands):
                    # Get the number of ways to build a bridge between the current island and the other island
                    num_ways *= num_islands - k
                    
                # Add the number of ways to build the current bridge to the total number of ways
                number_of_ways += num_ways
    
    # Return the total number of ways to build bridges, modulo 998 244 353
    return number_of_ways % 998244353

def main():
    # Read a line of input from stdin and split it into tokens
    a, b, c = map(int, input().split())
    
    # Call the get_number_of_ways function and print the result
    print(get_number_of_ways(a, b, c))

if __name__ == '__main__':
    main()


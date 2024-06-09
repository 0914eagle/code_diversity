
def get_number_of_ways(n, k, lamps):
    # Initialize a dictionary to store the number of ways for each lamp
    ways = {}
    
    # Iterate over each lamp
    for i in range(n):
        # Get the period of time for the current lamp
        period = lamps[i][1] - lamps[i][0] + 1
        
        # If the lamp is turned on, add it to the dictionary
        if period % k == 0:
            ways[i] = 1
        # If the lamp is turned off, add it to the dictionary with a value of 0
        else:
            ways[i] = 0
    
    # Initialize a variable to store the total number of ways
    total_ways = 1
    
    # Iterate over each lamp
    for i in range(n):
        # If the current lamp is turned on, multiply the total number of ways by the number of ways for the current lamp
        if ways[i] == 1:
            total_ways *= ways[i]
        # If the current lamp is turned off, divide the total number of ways by the number of ways for the current lamp
        else:
            total_ways //= ways[i]
    
    # Return the total number of ways modulo 998244353
    return total_ways % 998244353

def main():
    # Read the input data
    n, k = map(int, input().split())
    lamps = []
    for i in range(n):
        lamps.append(list(map(int, input().split())))
    
    # Call the get_number_of_ways function and print the result
    print(get_number_of_ways(n, k, lamps))

if __name__ == '__main__':
    main()


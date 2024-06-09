
import sys

def count_ways(snow_log):
    # Sort the snow log by the starting point of each range
    snow_log.sort(key=lambda x: x[0])
    
    # Initialize the number of ways to place the sensors as 0
    num_ways = 0
    
    # Iterate through the snow log
    for i in range(len(snow_log)):
        # Get the current range
        current_range = snow_log[i]
        
        # Check if the current range starts at 0
        if current_range[0] == 0:
            # If it does, increment the number of ways
            num_ways += 1
        
        # Check if the current range overlaps with the previous range
        if i > 0 and current_range[0] <= snow_log[i-1][1]:
            # If it does, increment the number of ways
            num_ways += 1
    
    # Return the number of ways
    return num_ways

def main():
    # Read the number of entries in the snow log
    n = int(input())
    
    # Read the snow log
    snow_log = []
    for i in range(n):
        a, b = map(int, input().split())
        snow_log.append([a, b])
    
    # Call the count_ways function and print the result
    result = count_ways(snow_log)
    print(result)

if __name__ == "__main__":
    main()


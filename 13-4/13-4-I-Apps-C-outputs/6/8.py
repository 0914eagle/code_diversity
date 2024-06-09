
import sys

def count_ways(snow_log):
    # Sort the snow log by the start point of each range
    snow_log.sort(key=lambda x: x[0])
    
    # Initialize the number of ways to place the sensors as 0
    num_ways = 0
    
    # Loop through each range in the snow log
    for i in range(len(snow_log)):
        # Get the start and end points of the current range
        start, end = snow_log[i][0], snow_log[i][1]
        
        # If the start point is greater than 0, we can place a sensor there
        if start > 0:
            num_ways += 1
        
        # If the end point is less than or equal to 0, we can place a sensor there
        if end <= 0:
            num_ways += 1
    
    # Return the number of ways to place the sensors
    return num_ways

def main():
    # Read the number of ranges of snowfall from stdin
    n = int(input())
    
    # Read the ranges of snowfall from stdin
    snow_log = []
    for i in range(n):
        a, b = map(int, input().split())
        snow_log.append([a, b])
    
    # Call the count_ways function to count the number of ways to place the sensors
    num_ways = count_ways(snow_log)
    
    # Print the number of ways to place the sensors
    print(num_ways % 1000000009)

if __name__ == "__main__":
    main()


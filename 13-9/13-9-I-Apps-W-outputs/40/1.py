
def get_minimum_time(sticks):
    # Sort the sticks in non-decreasing order
    sticks.sort()
    
    # Initialize the minimum time needed to form a triangle
    min_time = 0
    
    # Loop through the sticks and check if they can form a triangle
    for i in range(len(sticks)):
        if sticks[i] + sticks[i+1] > sticks[i+2]:
            # If the sticks can form a triangle, return the current minimum time
            return min_time
        else:
            # If the sticks cannot form a triangle, increment the minimum time by 1
            min_time += 1
    
    # If the loop completes and no triangle can be formed, return -1
    return -1

def main():
    # Read the input sticks from stdin
    a, b, c = map(int, input().split())
    
    # Create a list of sticks
    sticks = [a, b, c]
    
    # Call the get_minimum_time function and print the result
    print(get_minimum_time(sticks))

if __name__ == '__main__':
    main()


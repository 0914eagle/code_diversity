
def get_minimum_time(sticks):
    # Sort the sticks in non-decreasing order
    sticks.sort()
    
    # Initialize the minimum time to 0
    minimum_time = 0
    
    # Loop through the sticks and check if they can form a triangle
    for i in range(len(sticks)):
        for j in range(i+1, len(sticks)):
            for k in range(j+1, len(sticks)):
                if sticks[i] + sticks[j] > sticks[k]:
                    return minimum_time
    
    # If no triangle can be formed, return -1
    return -1

def main():
    # Read the sticks from stdin
    a, b, c = map(int, input().split())
    
    # Call the get_minimum_time function and print the result
    print(get_minimum_time([a, b, c]))

if __name__ == '__main__':
    main()


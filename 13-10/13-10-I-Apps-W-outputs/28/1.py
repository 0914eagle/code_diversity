
def solve(n, k, pebbles):
    # Initialize the number of days needed to collect all pebbles
    days = 0
    
    # Initialize the number of pebbles collected on each day
    collected = [0] * n
    
    # Loop through each day
    for day in range(n):
        # Determine the maximum number of pebbles that can be collected on this day
        max_collect = k - sum(collected)
        
        # If the maximum number of pebbles that can be collected on this day is greater than the number of pebbles of the current type, collect all the pebbles of the current type
        if max_collect > pebbles[day]:
            collected[day] = pebbles[day]
        # Otherwise, collect the maximum number of pebbles that can be collected on this day
        else:
            collected[day] = max_collect
        
        # Increment the number of days needed to collect all pebbles
        days += 1
    
    # Return the number of days needed to collect all pebbles
    return days

def main():
    # Read the number of pebble types and the maximum number of pebbles that can be placed in one pocket
    n, k = map(int, input().split())
    
    # Read the number of pebbles of each type
    pebbles = list(map(int, input().split()))
    
    # Determine the minimum number of days needed to collect all pebbles
    days = solve(n, k, pebbles)
    
    # Print the minimum number of days needed to collect all pebbles
    print(days)

if __name__ == '__main__':
    main()



def get_min_days(num_types, max_pebbles, pebbles):
    # Calculate the total number of pebbles
    total_pebbles = sum(pebbles)
    
    # Initialize the minimum number of days to collect all pebbles
    min_days = 0
    
    # Loop through each type of pebble
    for i in range(num_types):
        # Calculate the number of pebbles of the current type
        num_pebbles = pebbles[i]
        
        # Calculate the number of days needed to collect all pebbles of the current type
        days = num_pebbles // max_pebbles
        
        # If there are remaining pebbles, add an extra day
        if num_pebbles % max_pebbles != 0:
            days += 1
        
        # Update the minimum number of days to collect all pebbles
        min_days = max(min_days, days)
    
    return min_days

def main():
    # Read the input data
    num_types, max_pebbles = map(int, input().split())
    pebbles = list(map(int, input().split()))
    
    # Calculate the minimum number of days to collect all pebbles
    min_days = get_min_days(num_types, max_pebbles, pebbles)
    
    # Print the result
    print(min_days)

if __name__ == '__main__':
    main()


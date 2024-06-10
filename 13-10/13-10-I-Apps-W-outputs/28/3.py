
def get_minimum_days(n, k, pebbles):
    # Calculate the maximum number of pebbles that can be collected on each day
    max_pebbles_per_day = k * max(pebbles)
    
    # Calculate the total number of pebbles that need to be collected
    total_pebbles = sum(pebbles)
    
    # Initialize the number of days needed to collect all the pebbles
    days = 0
    
    # Loop through each pebble type and calculate the number of days needed to collect all the pebbles of that type
    for pebble in pebbles:
        # Calculate the number of full days needed to collect all the pebbles of this type
        full_days = pebble // max_pebbles_per_day
        
        # Calculate the number of partial days needed to collect the remaining pebbles of this type
        partial_days = 1 if pebble % max_pebbles_per_day != 0 else 0
        
        # Add the number of days needed for this type of pebble to the total number of days
        days += full_days + partial_days
    
    # Return the minimum number of days needed to collect all the pebbles
    return days

def main():
    n, k = map(int, input().split())
    pebbles = list(map(int, input().split()))
    print(get_minimum_days(n, k, pebbles))

if __name__ == '__main__':
    main()


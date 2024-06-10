
def get_min_days(n, k, w):
    # Calculate the total number of pebbles
    total_pebbles = sum(w)
    
    # Initialize the number of days needed to collect all pebbles
    days = 0
    
    # Loop through each pebble type
    for i in range(n):
        # Calculate the number of pebbles of the current type that can be collected on this day
        current_pebbles = min(k, w[i])
        
        # Add the number of pebbles of the current type to the total number of pebbles collected
        total_pebbles -= current_pebbles
        
        # Increment the number of days needed to collect all pebbles
        days += 1
        
        # If all pebbles have been collected, break the loop
        if total_pebbles == 0:
            break
    
    # Return the minimum number of days needed to collect all pebbles
    return days

def main():
    n, k = map(int, input().split())
    w = list(map(int, input().split()))
    print(get_min_days(n, k, w))

if __name__ == '__main__':
    main()


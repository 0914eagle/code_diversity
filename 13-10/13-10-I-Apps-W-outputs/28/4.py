
def get_number_of_days(n, k, w):
    # Calculate the total number of pebbles
    total_pebbles = sum(w)
    
    # Initialize the number of days to 0
    number_of_days = 0
    
    # Loop through each pebble type
    for i in range(n):
        # Calculate the number of pebbles of the current type that can be collected on this day
        current_pebbles = min(k, w[i])
        
        # Add the number of pebbles of the current type to the total number of pebbles collected so far
        total_pebbles -= current_pebbles
        
        # Increment the number of days if all the pebbles of the current type have been collected
        if total_pebbles < 0:
            number_of_days += 1
            total_pebbles += w[i]
    
    # Return the number of days needed to collect all the pebbles
    return number_of_days

def main():
    n, k = map(int, input().split())
    w = list(map(int, input().split()))
    print(get_number_of_days(n, k, w))

if __name__ == '__main__':
    main()


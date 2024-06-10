
def get_number_of_days(n, k, w):
    # Calculate the total number of pebbles
    total_pebbles = sum(w)
    
    # Initialize the number of days to 0
    days = 0
    
    # Loop through each pebble type
    for i in range(n):
        # Calculate the number of pebbles of the current type that can be collected in one day
        current_type_pebbles = min(k, w[i])
        
        # Add the number of days needed to collect all the pebbles of the current type
        days += (w[i] - 1) // current_type_pebbles + 1
    
    # Return the minimum number of days needed to collect all the pebbles
    return days

def main():
    # Read the input data
    n, k = map(int, input().split())
    w = list(map(int, input().split()))
    
    # Calculate the minimum number of days needed to collect all the pebbles
    days = get_number_of_days(n, k, w)
    
    # Print the result
    print(days)

if __name__ == '__main__':
    main()


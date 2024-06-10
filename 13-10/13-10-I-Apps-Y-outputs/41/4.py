
def get_max_days(a, b, c):
    # Initialize variables
    days = [0, 0, 0, 0, 0, 0, 0]
    max_days = 0
    
    # Iterate through the days of the week
    for i in range(7):
        # Check if the current day is a Monday, Thursday, or Sunday
        if i % 3 == 0:
            # Add the number of fish food portions to the current day
            days[i] += a
        # Check if the current day is a Tuesday or Saturday
        elif i % 2 == 0:
            # Add the number of rabbit stew portions to the current day
            days[i] += b
        # Check if the current day is any other day
        else:
            # Add the number of chicken stake portions to the current day
            days[i] += c
        
        # Update the maximum number of days the cat can eat
        max_days = max(max_days, max(days))
    
    # Return the maximum number of days the cat can eat
    return max_days

def main():
    # Read the input
    a, b, c = map(int, input().split())
    
    # Get the maximum number of days the cat can eat
    max_days = get_max_days(a, b, c)
    
    # Print the maximum number of days the cat can eat
    print(max_days)

if __name__ == '__main__':
    main()


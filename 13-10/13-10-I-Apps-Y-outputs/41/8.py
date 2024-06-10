
def get_days_eaten(a, b, c):
    # Initialize a list to store the number of days eaten for each day of the week
    days_eaten = [0, 0, 0, 0, 0, 0, 0]
    
    # Iterate through each day of the week
    for i in range(7):
        # Check if the current day is a Monday, Thursday, or Sunday
        if i % 2 == 0 or i == 6:
            # If the current day is a Monday, Thursday, or Sunday, the cat can eat fish food
            days_eaten[i] += a
        # Check if the current day is a Tuesday or Saturday
        elif i % 2 == 1:
            # If the current day is a Tuesday or Saturday, the cat can eat rabbit stew
            days_eaten[i] += b
        # Otherwise, the cat can eat chicken stakes
        else:
            days_eaten[i] += c
    
    # Return the maximum number of days the cat can eat without additional food purchases
    return max(days_eaten)

def get_optimal_day(a, b, c):
    # Initialize a variable to store the optimal day
    optimal_day = 0
    
    # Iterate through each day of the week
    for i in range(7):
        # Calculate the number of days eaten for the current day
        days_eaten = get_days_eaten(a, b, c)
        
        # Check if the current day is the optimal day
        if days_eaten > get_days_eaten(a, b, c)[optimal_day]:
            # If the current day is the optimal day, update the optimal day
            optimal_day = i
    
    # Return the optimal day
    return optimal_day

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(get_optimal_day(a, b, c))



def get_min_days(n, p, q, a, b):
    # Initialize variables
    days = 0
    exp = 0
    money = 0
    
    # Loop through each project
    for i in range(n):
        # Calculate the number of days needed for this project
        days_needed = (p - exp) / a[i]
        days_needed = ceil(days_needed)
        
        # Calculate the number of days needed for this project with the current money
        days_needed_money = (q - money) / b[i]
        days_needed_money = ceil(days_needed_money)
        
        # Choose the minimum number of days needed
        days_needed = min(days_needed, days_needed_money)
        
        # Update the experience and money
        exp += a[i] * days_needed
        money += b[i] * days_needed
        
        # Increment the number of days
        days += days_needed
    
    # Return the minimum number of days needed
    return days


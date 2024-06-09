
def get_min_days(n, p, q, a, b):
    # Initialize variables
    min_days = 0
    current_exp = 0
    current_money = 0
    
    # Loop through each project
    for i in range(n):
        # Calculate the number of days needed for this project
        days_needed = (p - current_exp) / a[i]
        days_needed = max(days_needed, 0)
        
        # Calculate the number of days needed for this project with the current money
        days_needed_money = (q - current_money) / b[i]
        days_needed_money = max(days_needed_money, 0)
        
        # Calculate the minimum number of days needed for this project
        days_needed = min(days_needed, days_needed_money)
        
        # Update the current experience and money
        current_exp += a[i] * days_needed
        current_money += b[i] * days_needed
        
        # Update the minimum number of days needed
        min_days = max(min_days, days_needed)
    
    return min_days


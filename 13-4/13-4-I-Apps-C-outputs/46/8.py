
def get_min_days(n, p, q, a, b):
    # Initialize variables
    min_days = 0
    curr_exp = 0
    curr_money = 0
    
    # Loop through each project
    for i in range(n):
        # Calculate the number of days needed for this project
        days = (p - curr_exp) / a[i]
        days = max(days, 0)
        
        # Calculate the number of days needed for this project with the current money
        days_with_money = (q - curr_money) / b[i]
        days_with_money = max(days_with_money, 0)
        
        # Calculate the minimum number of days needed for this project
        min_days_project = min(days, days_with_money)
        
        # Update the minimum number of days needed
        min_days = max(min_days, min_days_project)
        
        # Update the current experience and money
        curr_exp += a[i] * min_days_project
        curr_money += b[i] * min_days_project
    
    return min_days



def solve(n, firings, hirings):
    # Initialize the HR people as a list of tuples (id, days_handled)
    hr_people = [(i, 0) for i in range(1, n+1)]
    
    # Iterate through each day
    for i in range(n):
        # Get the number of firings and hirings for the current day
        f = firings[i]
        h = hirings[i]
        
        # Find the HR person with the least number of days handled
        min_days_handled = min(hr_people, key=lambda x: x[1])[1]
        
        # Assign the HR person to handle the firings and hirings for the current day
        hr_people[min_days_handled][1] += f + h
        
    # Return the smallest number of HR people needed
    return min(hr_people, key=lambda x: x[1])[0]


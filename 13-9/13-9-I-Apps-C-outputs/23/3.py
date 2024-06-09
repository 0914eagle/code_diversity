
def get_maximum_value(k, n, employees):
    # Sort the employees by their productivity in descending order
    employees.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the maximum total value and the current team size
    max_value = 0
    team_size = 0
    
    # Iterate through the employees
    for employee in employees:
        # If the employee's recommender is not in the team and is not the CEO, skip this employee
        if employee[2] not in team and employee[2] != 0:
            continue
        
        # Add the employee to the team
        team.append(employee)
        team_size += 1
        
        # If the team size is equal to k, break the loop
        if team_size == k:
            break
    
    # Calculate the maximum total value by dividing the sum of the productivities by the sum of the salaries
    max_value = sum([employee[1] for employee in team]) / sum([employee[0] for employee in team])
    
    # Return the maximum total value
    return round(max_value, 3)


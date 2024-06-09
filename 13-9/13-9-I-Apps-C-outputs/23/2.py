
def get_maximum_value(k, n, employees):
    # Sort the employees by their productivity in descending order
    employees.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the maximum total value and the current team size
    max_value, team_size = 0, 0
    
    # Iterate through the employees and add them to the team if they meet the criteria
    for employee in employees:
        if employee[2] == 0 or employee[2] in team:
            team.append(employee)
            team_size += 1
            max_value += employee[1] / employee[0]
            if team_size == k:
                break
    
    # Return the maximum total value
    return round(max_value, 3)


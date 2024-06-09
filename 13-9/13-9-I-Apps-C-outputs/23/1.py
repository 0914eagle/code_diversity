
def get_maximum_value(k, n, employees):
    # Sort the employees by their productivity in descending order
    employees.sort(key=lambda x: x[1], reverse=True)
    # Initialize the team with the CEO
    team = [0]
    # Initialize the total value of the team
    total_value = 0
    # Iterate through the employees
    for employee in employees:
        # If the employee is not the CEO and is not already in the team
        if employee[2] != 0 and employee[2] not in team:
            # Add the employee to the team
            team.append(employee[2])
            # Add the employee's productivity to the total value
            total_value += employee[1]
            # If the team is full, break the loop
            if len(team) == k:
                break
    # Return the total value divided by the sum of the employees' salaries
    return total_value / sum(employee[0] for employee in employees if employee[2] in team)


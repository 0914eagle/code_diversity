
def get_maximum_value(k, n, employees):
    # Sort the employees by their productivity in descending order
    employees.sort(key=lambda x: x[1], reverse=True)
    # Initialize the team with the CEO
    team = [0]
    # Initialize the total value of the team to 0
    total_value = 0
    # Iterate through the remaining employees
    for employee in employees:
        # If the employee is not the CEO and their recommender is not in the team, skip them
        if employee[2] != 0 and employee[2] not in team:
            continue
        # If the team is full, break the loop
        if len(team) == k:
            break
        # Add the employee to the team
        team.append(employee[0])
        # Update the total value of the team
        total_value += employee[1] / employee[0]
    # Return the total value of the team
    return round(total_value, 3)


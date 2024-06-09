
def get_maximum_value(k, n, employees):
    # Sort the employees by their productivity in descending order
    employees.sort(key=lambda x: x[1], reverse=True)

    # Initialize the maximum total value and the current team size
    max_value = 0
    team_size = 0

    # Iterate through the employees
    for employee in employees:
        # If the current employee is recommended by the CEO or by an employee who is already in the team, add them to the team
        if employee[2] == 0 or employee[2] in [employee[0] for employee in team]:
            team.append(employee)
            team_size += 1
            max_value += employee[1] / employee[0]

        # If the team size is equal to k, break the loop
        if team_size == k:
            break

    # Return the maximum total value
    return round(max_value, 3)



def get_maximum_total_value(k, n, employees):
    # Sort the employees by their productivity in descending order
    employees.sort(key=lambda x: x[1], reverse=True)
    # Initialize the maximum total value and the current team size
    max_total_value = 0
    current_team_size = 0
    # Iterate through the employees
    for employee in employees:
        # If the current team size is less than the maximum team size and the employee's recommender is in the team or is the CEO
        if current_team_size < k and (employee[2] in [0, employees[i][0] for i in range(len(employees)) if employees[i][0] in current_team_size]):
            # Add the employee to the team and update the maximum total value
            current_team_size += 1
            max_total_value += employee[1] / employee[0]
    # Return the maximum total value
    return round(max_total_value, 3)


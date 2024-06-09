
def get_maximum_value(k, n, employees):
    # Sort the employees by their productivity in descending order
    employees.sort(key=lambda x: x[1], reverse=True)
    # Create a dictionary to store the employees and their recommender
    employee_dict = {employee[0]: employee[2] for employee in employees}
    # Initialize the maximum total value and the current team size
    max_value, team_size = 0, 0
    # Iterate through the employees and add them to the team if possible
    for employee in employees:
        # If the current employee is the CEO or their recommender is already in the team, add them to the team
        if employee[0] == 0 or employee_dict[employee[0]] in employee_dict:
            team_size += 1
            max_value += employee[1] / employee[0]
            # If the team size reaches k, break the loop
            if team_size == k:
                break
    # Return the maximum total value
    return round(max_value, 3)


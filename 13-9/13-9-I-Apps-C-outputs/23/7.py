
def get_max_value(k, n, employees):
    # Sort the employees by their productivity in descending order
    employees.sort(key=lambda x: x[1], reverse=True)

    # Create a dictionary to store the employees and their recommender
    employee_dict = {}
    for employee in employees:
        employee_dict[employee[0]] = employee[2]

    # Initialize the team with the CEO
    team = [0]
    total_value = 0

    # Iterate through the employees and add them to the team if their recommender is also in the team or is the CEO
    for employee in employees:
        if employee[0] in team or employee_dict[employee[0]] == 0:
            team.append(employee[0])
            total_value += employee[1] / employee[0]

        # If the team is full, break the loop
        if len(team) == k:
            break

    # Return the total value of the team
    return round(total_value, 3)


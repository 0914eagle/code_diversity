
def get_max_value(k, n, employees):
    # Sort the employees by their productivity in descending order
    employees.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the maximum total value and the current team size
    max_value = 0
    current_size = 0
    
    # Iterate through the employees
    for employee in employees:
        # If the current team size is less than or equal to k and the employee's recommender is part of the team or is the CEO, add the employee to the team
        if current_size <= k and (employee[2] in [0] + [emp[0] for emp in employees[:current_size]]):
            current_size += 1
            max_value += employee[1] / employee[0]
    
    # Return the maximum total value
    return round(max_value, 3)


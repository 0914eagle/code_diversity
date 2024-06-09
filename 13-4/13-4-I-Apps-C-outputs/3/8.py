
def get_immediate_boss_and_subordinates(employees, query):
    # Sort the employees by salary in descending order
    employees.sort(key=lambda x: x[1], reverse=True)
    
    # Create a dictionary to map employee ID to their details
    employee_dict = {employee[0]: employee for employee in employees}
    
    # Initialize the result dictionary
    result = {}
    
    # Iterate over the employees
    for employee in employees:
        # Get the current employee's ID, salary, and height
        employee_id, salary, height = employee
        
        # Find the immediate boss of the current employee
        for other_employee in employees:
            # Get the other employee's ID, salary, and height
            other_employee_id, other_employee_salary, other_employee_height = other_employee
            
            # Check if the other employee is the immediate boss of the current employee
            if other_employee_salary < salary and other_employee_height >= height:
                # Add the current employee to the result dictionary with their immediate boss's ID and number of subordinates
                result[employee_id] = (other_employee_id, len(employee_dict[other_employee_id][2]))
                break
        else:
            # If no immediate boss is found, set the current employee's immediate boss to 0 and number of subordinates to 0
            result[employee_id] = (0, 0)
    
    # Return the result for the query employee ID
    return result[query]


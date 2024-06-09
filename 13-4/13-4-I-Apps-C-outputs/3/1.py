
def get_immediate_boss_and_subordinates(employees, query):
    # Sort the employees by salary in descending order
    employees.sort(key=lambda x: x[1], reverse=True)
    
    # Create a dictionary to map employee ID to index in the list of employees
    employee_map = {employee[0]: i for i, employee in enumerate(employees)}
    
    # Initialize the list of subordinates for each employee
    subordinates = [[] for _ in range(len(employees))]
    
    # Loop through the employees and find the immediate boss for each employee
    for i, employee in enumerate(employees):
        # Find the index of the employee's immediate boss
        boss_index = i
        while boss_index > 0 and employees[boss_index - 1][2] >= employee[2]:
            boss_index -= 1
        
        # Add the employee to the list of subordinates for their immediate boss
        subordinates[boss_index].append(employee[0])
    
    # Find the immediate boss and number of subordinates for the query employee
    query_index = employee_map[query]
    boss_id = employees[query_index - 1][0] if query_index > 0 else 0
    num_subordinates = len(subordinates[query_index])
    
    return boss_id, num_subordinates


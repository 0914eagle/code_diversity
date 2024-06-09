
def get_immediate_boss_and_subordinates(employees, queries):
    # Create a dictionary to store the employees and their information
    employees_dict = {}
    for employee in employees:
        employees_dict[employee[0]] = (employee[1], employee[2])
    
    # Create a dictionary to store the bosses and their subordinates
    bosses_dict = {}
    for employee in employees:
        bosses_dict[employee[0]] = []
    
    # Populate the bosses and subordinates dictionary
    for employee in employees:
        # If the employee is the chairperson, they have no boss
        if employee[0] == 123456:
            continue
        
        # Find the boss of the current employee
        boss_id = get_boss_id(employees_dict, employee[0])
        
        # Add the current employee to the list of subordinates of their boss
        bosses_dict[boss_id].append(employee[0])
    
    # Create a list to store the answers to the queries
    answers = []
    
    # Iterate through the queries and find the immediate boss and number of subordinates for each employee
    for query in queries:
        # If the query is the ID of the chairperson, they have no boss
        if query == 123456:
            answers.append((0, 0))
            continue
        
        # Find the immediate boss of the current employee
        boss_id = get_boss_id(employees_dict, query)
        
        # Find the number of subordinates of the current employee
        num_subordinates = len(bosses_dict[query])
        
        answers.append((boss_id, num_subordinates))
    
    return answers

def get_boss_id(employees_dict, employee_id):
    # Find the boss of the current employee by finding the employee who earns the least among all the employees that earn more than the current employee and are at least as tall as the current employee
    boss_id = None
    for employee in employees_dict:
        if employee != employee_id and employees_dict[employee][0] > employees_dict[employee_id][0] and employees_dict[employee][1] >= employees_dict[employee_id][1]:
            if boss_id == None or employees_dict[employee][0] < employees_dict[boss_id][0]:
                boss_id = employee
    
    return boss_id



def get_boss_and_subordinates(employees, query):
    # Initialize a dictionary to store the boss and subordinates for each employee
    boss_and_subordinates = {}

    # Iterate over the employees and their salaries and heights
    for employee, salary, height in employees:
        # If the employee is the chairperson, set their boss to 0 and subordinates to 0
        if employee == query:
            boss_and_subordinates[employee] = (0, 0)
            continue

        # Find the boss for the current employee by finding the employee who earns the least and is at least as tall as the current employee
        boss = None
        for boss_candidate, boss_candidate_salary, boss_candidate_height in employees:
            if boss_candidate_salary < salary and boss_candidate_height >= height:
                boss = boss_candidate
                break

        # If the boss is not found, set the boss to 0
        if boss is None:
            boss = 0

        # Find the number of subordinates for the current employee by counting the number of employees who are at least as tall as the current employee and have a higher salary than the current employee
        subordinates = 0
        for employee_candidate, employee_candidate_salary, employee_candidate_height in employees:
            if employee_candidate_height >= height and employee_candidate_salary > salary:
                subordinates += 1

        # Add the boss and subordinates for the current employee to the dictionary
        boss_and_subordinates[employee] = (boss, subordinates)

    # Return the boss and subordinates for the query employee
    return boss_and_subordinates[query]


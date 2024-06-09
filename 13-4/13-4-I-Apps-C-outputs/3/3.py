
def get_boss_and_subordinates(employees, query):
    # Initialize a dictionary to store the boss and subordinates for each employee
    boss_and_subordinates = {}

    # Iterate over the employees and their salaries and heights
    for employee, salary, height in employees:
        # Find the boss for this employee by finding the employee who earns the least among all employees who are at least as tall as this employee and earn more than this employee
        boss = None
        for other_employee, other_salary, other_height in employees:
            if other_employee != employee and other_salary > salary and other_height >= height:
                boss = other_employee
                break

        # Add the boss and subordinates for this employee to the dictionary
        boss_and_subordinates[employee] = (boss, 0)

    # Iterate over the queries and return the boss and subordinates for each employee
    for employee in query:
        boss, subordinates = boss_and_subordinates[employee]
        yield (boss, subordinates)


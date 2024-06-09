
def get_boss_and_subordinates(employees, query):
    # Initialize a dictionary to store the boss and subordinates for each employee
    boss_and_subordinates = {}

    # Iterate over the employees and their salaries and heights
    for employee, salary, height in employees:
        # If the employee is the chairperson, set their boss to 0 and subordinates to 0
        if employee == query:
            boss_and_subordinates[employee] = (0, 0)
            continue

        # Find the employee's boss by finding the employee with the least salary who is at least as tall as the current employee
        boss = None
        for boss_candidate, boss_candidate_salary, boss_candidate_height in employees:
            if boss_candidate_salary <= salary and boss_candidate_height >= height:
                boss = boss_candidate
                break

        # If the employee has no boss, set their subordinates to 0
        if boss is None:
            boss_and_subordinates[employee] = (0, 0)
        else:
            # Find the number of subordinates by counting the number of employees who are at least as tall as the current employee and have a salary less than their boss
            subordinates = 0
            for subordinate, subordinate_salary, subordinate_height in employees:
                if subordinate_height >= height and subordinate_salary < boss_and_subordinates[boss][0]:
                    subordinates += 1

            # Set the boss and subordinates for the current employee
            boss_and_subordinates[employee] = (boss, subordinates)

    # Return the boss and subordinates for the query employee
    return boss_and_subordinates[query]


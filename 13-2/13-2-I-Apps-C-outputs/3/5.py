
def get_invited_employees(teams, my_id):
    # Initialize a set to store the IDs of employees to invite
    invited_employees = set()
    # Add the ID of the friend to the set
    invited_employees.add(my_id)
    # Iterate through the teams
    for team in teams:
        # If the team has both employees from Stockholm and London, skip it
        if team[0] // 1000 == team[1] // 1000:
            continue
        # Add the ID of the employee from the other city to the set
        invited_employees.add(team[0] if team[0] // 1000 == 1 else team[1])
    # Return the set of invited employees
    return invited_employees


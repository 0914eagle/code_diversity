
def get_smallest_number_of_invitees(teams, my_id):
    # Initialize a set to store the IDs of the employees to invite
    invitees = set()
    # Add the ID of the friend to the set of invitees
    invitees.add(my_id)
    # Iterate over the teams
    for team in teams:
        # If the ID of the employee from Stockholm is not in the set of invitees, add it
        if team[0] not in invitees:
            invitees.add(team[0])
        # If the ID of the employee from London is not in the set of invitees, add it
        if team[1] not in invitees:
            invitees.add(team[1])
    # Return the length of the set of invitees
    return len(invitees)


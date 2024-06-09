
def get_invitees(teams, my_id):
    # Initialize a set to store the IDs of the employees to invite
    invitees = set()
    
    # Iterate over the teams
    for team in teams:
        # If the team does not contain my_id, add it to the set of invitees
        if my_id not in team:
            invitees.add(team[0])
    
    # Return the set of invitees
    return invitees



def get_invitees(teams, my_id):
    # Initialize a set to store the IDs of the employees to invite
    invitees = set()
    
    # Add the ID of the friend to the set of invitees
    invitees.add(my_id)
    
    # Iterate over the teams
    for team in teams:
        # If the team does not contain the friend, add its members to the set of invitees
        if my_id not in team:
            invitees.update(team)
    
    # Return the set of invitees
    return invitees


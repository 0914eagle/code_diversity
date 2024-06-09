
def get_smallest_number_of_invitees(teams, friend_id):
    # Initialize a set to store the IDs of the employees to invite
    invitees = set()
    
    # Iterate over the teams
    for team in teams:
        # If the friend is not in the team, add both team members to the invitees set
        if friend_id not in team:
            invitees.update(team)
    
    # Return the length of the invitees set, which is the smallest number of invitees needed
    return len(invitees)



def get_smallest_number_of_invitees(teams, friend_id):
    # Initialize a set to store the IDs of the employees to invite
    invitees = set()
    # Add the friend's ID to the set
    invitees.add(friend_id)
    # Iterate over the teams
    for team in teams:
        # If the team does not contain the friend's ID, add it to the set
        if friend_id not in team:
            invitees.update(team)
    # Return the length of the set (i.e., the number of employees to invite)
    return len(invitees)

def get_invitee_ids(teams, friend_id):
    # Call the first function to get the smallest number of invitees
    num_invitees = get_smallest_number_of_invitees(teams, friend_id)
    # Initialize a list to store the IDs of the employees to invite
    invitee_ids = []
    # Iterate over the teams
    for team in teams:
        # If the team contains the friend's ID, add it to the list
        if friend_id in team:
            invitee_ids.append(friend_id)
        # If the team does not contain the friend's ID, add the first employee's ID to the list
        else:
            invitee_ids.append(team[0])
    # Return the list of invitee IDs
    return invitee_ids

if __name__ == '__main__':
    # Read the number of teams from stdin
    num_teams = int(input())
    # Read the teams from stdin
    teams = []
    for _ in range(num_teams):
        team = list(map(int, input().split()))
        teams.append(team)
    # Get the ID of the friend
    friend_id = 1009
    # Call the second function to get the list of invitee IDs
    invitee_ids = get_invitee_ids(teams, friend_id)
    # Print the number of invitees
    print(len(invitee_ids))
    # Print the list of invitee IDs
    for invitee_id in invitee_ids:
        print(invitee_id)


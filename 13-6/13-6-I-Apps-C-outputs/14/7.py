
def get_smallest_number_of_invites(teams, my_id):
    # Initialize a set to store the IDs of employees to invite
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
    # Return the length of the set of invitees, which is the smallest number of employees to invite
    return len(invitees)

def get_invitees(teams, my_id):
    # Call the function to get the smallest number of invitees
    num_invitees = get_smallest_number_of_invites(teams, my_id)
    # Initialize a list to store the IDs of the invitees
    invitees = []
    # Iterate over the teams
    for team in teams:
        # If the ID of the employee from Stockholm is in the set of invitees, add it to the list of invitees
        if team[0] in invitees:
            invitees.append(team[0])
        # If the ID of the employee from London is in the set of invitees, add it to the list of invitees
        if team[1] in invitees:
            invitees.append(team[1])
    # Return the list of invitees
    return invitees

if __name__ == '__main__':
    # Read the number of teams from stdin
    num_teams = int(input())
    # Read the teams from stdin
    teams = []
    for _ in range(num_teams):
        teams.append(tuple(map(int, input().split())))
    # Get the ID of the friend from stdin
    my_id = int(input())
    # Call the function to get the smallest number of invitees
    num_invitees = get_smallest_number_of_invites(teams, my_id)
    # Call the function to get the list of invitees
    invitees = get_invitees(teams, my_id)
    # Print the number of invitees
    print(num_invitees)
    # Print the list of invitees
    for invitee in invitees:
        print(invitee)


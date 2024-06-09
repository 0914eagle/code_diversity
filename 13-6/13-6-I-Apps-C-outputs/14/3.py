
def get_smallest_number_of_invitees(teams, friend_id):
    # Initialize a set to store the IDs of the invitees
    invitees = set()
    # Add the friend's ID to the set of invitees
    invitees.add(friend_id)
    # Iterate through the teams
    for team in teams:
        # If the team has both a Stockholm and a London employee, and neither of them is already in the set of invitees, add them to the set of invitees
        if team[0] >= 1000 and team[0] <= 1999 and team[1] >= 2000 and team[1] <= 2999 and team[0] not in invitees and team[1] not in invitees:
            invitees.add(team[0])
            invitees.add(team[1])
    # Return the length of the set of invitees, which is the smallest number of invitees needed to meet the requirements
    return len(invitees)

def get_invitee_ids(teams, friend_id):
    # Call the function to get the smallest number of invitees needed to meet the requirements
    num_invitees = get_smallest_number_of_invitees(teams, friend_id)
    # Initialize an empty list to store the IDs of the invitees
    invitee_ids = []
    # Iterate through the teams
    for team in teams:
        # If the team has both a Stockholm and a London employee, and neither of them is already in the list of invitees, add them to the list of invitees
        if team[0] >= 1000 and team[0] <= 1999 and team[1] >= 2000 and team[1] <= 2999 and team[0] not in invitee_ids and team[1] not in invitee_ids:
            invitee_ids.append(team[0])
            invitee_ids.append(team[1])
    # Return the list of invitee IDs
    return invitee_ids[:num_invitees]

if __name__ == '__main__':
    # Read the number of teams from stdin
    num_teams = int(input())
    # Read the teams from stdin
    teams = []
    for _ in range(num_teams):
        teams.append(list(map(int, input().split())))
    # Read the ID of the friend from stdin
    friend_id = int(input())
    # Call the function to get the list of invitee IDs
    invitee_ids = get_invitee_ids(teams, friend_id)
    # Print the number of invitees needed to meet the requirements
    print(len(invitee_ids))
    # Print the list of invitee IDs
    for invitee_id in invitee_ids:
        print(invitee_id)


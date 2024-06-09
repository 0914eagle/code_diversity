
def get_smallest_number_of_invitees(teams, my_id):
    # Initialize a set to store the IDs of the invitees
    invitees = set()
    # Add the ID of the friend to the set of invitees
    invitees.add(my_id)
    # Iterate through the teams
    for team in teams:
        # If the team has not already been invited, add its members to the set of invitees
        if team not in invitees:
            invitees.update(team)
    # Return the length of the set of invitees, which is the smallest number of invitees necessary to meet the requirements
    return len(invitees)

def get_invitees(teams, my_id):
    # Initialize a set to store the IDs of the invitees
    invitees = set()
    # Add the ID of the friend to the set of invitees
    invitees.add(my_id)
    # Iterate through the teams
    for team in teams:
        # If the team has not already been invited, add its members to the set of invitees
        if team not in invitees:
            invitees.update(team)
    # Return the set of invitees
    return invitees

def main():
    # Read the number of teams from stdin
    num_teams = int(input())
    # Read the teams from stdin
    teams = []
    for _ in range(num_teams):
        team = set(map(int, input().split()))
        teams.append(team)
    # Read the ID of the friend from stdin
    my_id = int(input())
    # Get the smallest number of invitees necessary to meet the requirements
    num_invitees = get_smallest_number_of_invitees(teams, my_id)
    # Get the set of invitees
    invitees = get_invitees(teams, my_id)
    # Print the number of invitees
    print(num_invitees)
    # Print the IDs of the invitees
    for invitee in invitees:
        print(invitee)

if __name__ == "__main__":
    main()


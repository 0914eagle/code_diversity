
def get_smallest_number_of_invitees(teams, my_id):
    # Initialize a set to store the IDs of the invitees
    invitees = set()
    # Add the ID of the friend
    invitees.add(my_id)
    # Loop through the teams
    for team in teams:
        # If the team has both IDs from Stockholm and London, skip it
        if team[0] // 1000 == team[1] // 1000:
            continue
        # Add the ID of the employee from the other city to the invitees set
        invitees.add(team[0] if team[0] // 1000 == 1 else team[1])
    # Return the length of the invitees set, which is the smallest number of invitees needed
    return len(invitees)

def get_invitees(teams, my_id):
    # Call the function to get the smallest number of invitees
    k = get_smallest_number_of_invitees(teams, my_id)
    # Initialize a list to store the IDs of the invitees
    invitees = []
    # Loop through the teams
    for team in teams:
        # If the team has both IDs from Stockholm and London, skip it
        if team[0] // 1000 == team[1] // 1000:
            continue
        # Add the ID of the employee from the other city to the invitees list
        invitees.append(team[0] if team[0] // 1000 == 1 else team[1])
    # Shuffle the list of invitees to randomize the order
    import random
    random.shuffle(invitees)
    # Return the first k elements of the list, which are the invitees
    return invitees[:k]

if __name__ == '__main__':
    # Read the number of teams and the teams from stdin
    num_teams = int(input())
    teams = []
    for _ in range(num_teams):
        teams.append(tuple(map(int, input().split())))
    # Get the ID of the friend from stdin
    my_id = int(input())
    # Call the function to get the invitees
    invitees = get_invitees(teams, my_id)
    # Print the number of invitees
    print(len(invitees))
    # Print the IDs of the invitees
    for invitee in invitees:
        print(invitee)



def get_smallest_number_of_people(team_list, my_id):
    # Initialize a set to store the IDs of the people to invite
    invited_ids = set()
    # Initialize a variable to store the smallest number of people to invite
    min_people = float('inf')
    # Loop through each team
    for team in team_list:
        # If the team does not contain my ID, add the IDs of the team members to the set of invited IDs
        if my_id not in team:
            invited_ids.update(team)
        # If the team contains my ID, add the IDs of the other team member to the set of invited IDs
        else:
            invited_ids.add(team[0] if team[1] == my_id else team[1])
        # Update the smallest number of people to invite if the current number of invited IDs is smaller than the minimum
        min_people = min(min_people, len(invited_ids))
    # Return the smallest number of people to invite
    return min_people

def get_invited_ids(team_list, my_id, min_people):
    # Initialize a set to store the IDs of the people to invite
    invited_ids = set()
    # Loop through each team
    for team in team_list:
        # If the team contains my ID, add the IDs of the other team member to the set of invited IDs
        if my_id in team:
            invited_ids.add(team[0] if team[1] == my_id else team[1])
    # Return the set of invited IDs
    return invited_ids

def main():
    # Read the number of teams from stdin
    num_teams = int(input())
    # Read the team information from stdin
    team_list = []
    for _ in range(num_teams):
        team_list.append(tuple(map(int, input().split())))
    # Get the ID of the person running the program
    my_id = 1009
    # Get the smallest number of people to invite
    min_people = get_smallest_number_of_people(team_list, my_id)
    # Get the set of IDs of the people to invite
    invited_ids = get_invited_ids(team_list, my_id, min_people)
    # Print the number of people to invite
    print(min_people)
    # Print the IDs of the people to invite
    for id in sorted(invited_ids):
        print(id)

if __name__ == '__main__':
    main()


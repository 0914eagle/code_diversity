
def get_min_teams_not_starting(num_teams, num_damaged, num_reserve, damaged_teams, reserve_teams):
    # Initialize a set to store the teams that cannot start
    cannot_start = set()

    # Loop through the damaged teams and their adjacent teams
    for damaged_team in damaged_teams:
        for team in range(damaged_team-1, damaged_team+2):
            # If the team has a reserve kayak, add it to the cannot_start set
            if team in reserve_teams:
                cannot_start.add(team)

    # Return the size of the cannot_start set
    return len(cannot_start)


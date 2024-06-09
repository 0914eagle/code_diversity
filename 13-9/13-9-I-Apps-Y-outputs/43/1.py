
def min_teams_not_starting(N, S, R, damaged_teams, reserve_teams):
    # Initialize a set to store the teams that cannot start
    cannot_start = set()

    # Iterate over the damaged teams and their reserve teams
    for damaged_team in damaged_teams:
        for reserve_team in reserve_teams:
            # If the reserve team is next to the damaged team, add it to the cannot start set
            if abs(reserve_team - damaged_team) == 1:
                cannot_start.add(reserve_team)

    # Return the number of teams that cannot start
    return len(cannot_start)


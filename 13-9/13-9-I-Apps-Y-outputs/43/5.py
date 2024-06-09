
def solve(N, S, R, damaged_teams, reserve_teams):
    # Initialize a set to store the teams that cannot start
    cannot_start = set()

    # Iterate over the damaged teams and their adjacent teams
    for team in damaged_teams:
        for adj_team in range(team-1, team+2):
            # If the adjacent team has a reserve kayak, add it to the cannot_start set
            if adj_team in reserve_teams:
                cannot_start.add(adj_team)

    # Return the size of the cannot_start set
    return len(cannot_start)


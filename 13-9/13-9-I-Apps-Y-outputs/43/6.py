
def solve(N, S, R, damaged, reserve):
    # Initialize a set to store the teams that cannot start
    cannot_start = set()

    # Iterate over the teams with damaged kayaks
    for team in damaged:
        # If the team is not in the list of teams with reserve kayaks, it cannot start
        if team not in reserve:
            cannot_start.add(team)

    # Iterate over the teams with reserve kayaks
    for team in reserve:
        # If the team is not in the list of teams with damaged kayaks, it can start
        if team not in damaged:
            # If the team's starting position is next to a team that cannot start, it cannot start
            if (team - 1) in cannot_start or (team + 1) in cannot_start:
                cannot_start.add(team)

    # Return the size of the set of teams that cannot start
    return len(cannot_start)


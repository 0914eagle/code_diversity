
def solve(N, S, R, damaged, reserved):
    # Initialize a set to store the teams that cannot start
    cannot_start = set()

    # Iterate over the teams with damaged kayaks
    for team in damaged:
        # If the team has a reserve kayak, it can start
        if team in reserved:
            continue
        # Otherwise, it cannot start
        cannot_start.add(team)

    # Iterate over the teams with reserve kayaks
    for team in reserved:
        # If the team has a damaged kayak, it cannot start
        if team in damaged:
            cannot_start.add(team)
        # Otherwise, it can start
        else:
            continue

    # Return the smallest number of teams that cannot start
    return len(cannot_start)


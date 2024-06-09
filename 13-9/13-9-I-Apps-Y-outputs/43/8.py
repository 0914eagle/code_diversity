
def solve(N, S, R, damaged, reserves):
    # Initialize a set to store the teams that cannot start
    cannot_start = set()

    # Iterate over the teams with damaged kayaks
    for team in damaged:
        # If the team is not in the set of teams with reserves, it cannot start
        if team not in reserves:
            cannot_start.add(team)

    # Iterate over the teams with reserves
    for team in reserves:
        # If the team is not in the set of teams with damaged kayaks, it can start
        if team not in damaged:
            # Find the team number that is immediately next to the current team
            next_team = (team + 1) % N
            # If the team number is in the set of teams with damaged kayaks, it cannot start
            if next_team in damaged:
                cannot_start.add(team)

    # Return the smallest number of teams that cannot start
    return len(cannot_start)


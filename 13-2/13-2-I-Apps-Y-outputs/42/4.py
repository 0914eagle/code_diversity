
def solve(n, runners):
    # Sort the runners by their time for the 1st leg in descending order
    runners.sort(key=lambda x: x[1], reverse=True)

    # Initialize the team with the fastest runner for the 1st leg
    team = [runners[0]]

    # Iterate over the remaining runners
    for runner in runners[1:]:
        # If the runner's time for the 1st leg is faster than the current team's time, replace the team with the current runner and continue
        if runner[1] < team[0][1]:
            team = [runner]
        # If the runner's time for the 2nd leg is faster than the current team's time, add the runner to the team
        elif runner[2] < team[0][2]:
            team.append(runner)

    # Sort the team by their time for the 1st leg in descending order
    team.sort(key=lambda x: x[1], reverse=True)

    # Return the team and the total time of the team
    return team, sum(runner[1] for runner in team)


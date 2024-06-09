
def solve(n, runners):
    # Sort the runners by their time for the 1st leg in descending order
    runners.sort(key=lambda x: x[1], reverse=True)

    # Initialize the team with the fastest runner for the 1st leg
    team = [runners[0]]

    # Iterate over the remaining runners
    for runner in runners[1:]:
        # If the runner's time for the 1st leg is faster than the current team's time, replace the team with the current runner for the 1st leg
        if runner[1] < team[0][1]:
            team = [runner]
        # If the runner's time for the 1st leg is equal to the current team's time, add the runner to the team
        elif runner[1] == team[0][1]:
            team.append(runner)

    # Sort the team by their time for the 2nd leg in ascending order
    team.sort(key=lambda x: x[2])

    # Initialize the team time with the sum of the 1st leg times
    team_time = sum([runner[1] for runner in team])

    # Iterate over the team members
    for i in range(len(team)):
        # If the runner's time for the 2nd leg is faster than the current team time, replace the team time with the current runner for the 2nd leg
        if team[i][2] < team_time:
            team_time = team[i][2]

    return team_time, team


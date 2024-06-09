
def solve(n, runners):
    # Sort the runners by their fastest leg time in descending order
    runners.sort(key=lambda x: x[1], reverse=True)

    # Initialize the team with the fastest runner for the first leg
    team = [runners[0]]

    # Iterate through the remaining runners
    for runner in runners[1:]:
        # If the runner's fastest leg time is faster than the current team's total time,
        # add them to the team and break
        if runner[1] < team[0][1]:
            team.append(runner)
            break

    # If the team is not full, add the remaining runners to the team
    for runner in runners[len(team):]:
        team.append(runner)

    # Calculate the total team time
    total_time = sum([runner[1] for runner in team])

    # Return the team and total time
    return team, total_time



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
        # If the runner's time for the 1st leg is the same as the current team's time, add the runner to the team
        elif runner[1] == team[0][1]:
            team.append(runner)
    
    # Sort the team by their time for the other legs in descending order
    team.sort(key=lambda x: x[2], reverse=True)
    
    # Return the team and their times
    return team



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
    
    # Sort the team by their time for the 2nd leg in descending order
    team.sort(key=lambda x: x[2], reverse=True)
    
    # Initialize the team with the fastest runner for the 2nd leg
    team2 = [team[0]]
    
    # Iterate over the remaining runners
    for runner in team[1:]:
        # If the runner's time for the 2nd leg is faster than the current team's time, replace the team with the current runner for the 2nd leg
        if runner[2] < team2[0][2]:
            team2 = [runner]
        # If the runner's time for the 2nd leg is equal to the current team's time, add the runner to the team
        elif runner[2] == team2[0][2]:
            team2.append(runner)
    
    # Sort the team by their time for the 3rd leg in descending order
    team2.sort(key=lambda x: x[2], reverse=True)
    
    # Initialize the team with the fastest runner for the 3rd leg
    team3 = [team2[0]]
    
    # Iterate over the remaining runners
    for runner in team2[1:]:
        # If the runner's time for the 3rd leg is faster than the current team's time, replace the team with the current runner for the 3rd leg
        if runner[2] < team3[0][2]:
            team3 = [runner]
        # If the runner's time for the 3rd leg is equal to the current team's time, add the runner to the team
        elif runner[2] == team3[0][2]:
            team3.append(runner)
    
    # Sort the team by their time for the 4th leg in descending order
    team3.sort(key=lambda x: x[2], reverse=True)
    
    # Initialize the team with the fastest runner for the 4th leg
    team4 = [team3[0]]
    
    # Iterate over the remaining runners
    for runner in team3[1:]:
        # If the runner's time for the 4th leg is faster than the current team's time, replace the team with the current runner for the 4th leg
        if runner[2] < team4[0][2]:
            team4 = [runner]
        # If the runner's time for the 4th leg is equal to the current team's time, add the runner to the team
        elif runner[2] == team4[0][2]:
            team4.append(runner)
    
    # Calculate the total time for the team
    total_time = team[0][1] + team2[0][2] + team3[0][2] + team4[0][2]
    
    # Return the team and the total time
    return team, total_time


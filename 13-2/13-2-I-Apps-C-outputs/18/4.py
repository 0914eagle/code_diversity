
def is_interesting_problemset(problems, teams):
    # Calculate the total number of problems known by each team
    team_problems = [sum(team) for team in teams]
    
    # Calculate the maximum number of problems that can be known by any team
    max_team_problems = max(team_problems)
    
    # Check if the maximum number of problems is less than or equal to the half of the total number of problems
    if max_team_problems <= len(problems) // 2:
        return "YES"
    else:
        return "NO"


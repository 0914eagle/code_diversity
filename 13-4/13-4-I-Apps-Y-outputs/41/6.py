
def solve(n, k, a):
    # Initialize two empty lists to store the teams
    team_1 = []
    team_2 = []
    
    # Sort the list of programming skills in descending order
    a.sort(reverse=True)
    
    # Iterate through the list of programming skills
    for i in range(n):
        # If the current student has a skill that is not already in either team
        if a[i] not in team_1 and a[i] not in team_2:
            # Add the current student to the first team
            team_1.append(a[i])
        # If the current student has a skill that is already in the first team
        elif a[i] in team_1:
            # Add the current student to the second team
            team_2.append(a[i])
    
    # Return the teams as a string of 1s and 2s
    return "".join([str(i) for i in team_1]) + "".join([str(i) for i in team_2])


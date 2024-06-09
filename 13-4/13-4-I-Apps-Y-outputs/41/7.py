
def solve(n, k, a):
    # Initialize two empty lists to store the teams
    team_1 = []
    team_2 = []
    
    # Sort the list of programming skills in descending order
    a.sort(reverse=True)
    
    # Loop through the list of programming skills
    for i in range(n):
        # If the current student is not in any team, choose them
        if i not in team_1 and i not in team_2:
            # Add the current student to the first team
            team_1.append(i)
            # Add the k closest students to the left and right of the current student to the first team
            for j in range(1, k+1):
                if i-j >= 0 and i-j not in team_1:
                    team_1.append(i-j)
                if i+j < n and i+j not in team_1:
                    team_1.append(i+j)
        
        # If the current student is not in any team, choose them
        if i not in team_1 and i not in team_2:
            # Add the current student to the second team
            team_2.append(i)
            # Add the k closest students to the left and right of the current student to the second team
            for j in range(1, k+1):
                if i-j >= 0 and i-j not in team_2:
                    team_2.append(i-j)
                if i+j < n and i+j not in team_2:
                    team_2.append(i+j)
    
    # Return the teams as a string of 1s and 2s
    return "".join([str(1 if i in team_1 else 2) for i in range(n)])


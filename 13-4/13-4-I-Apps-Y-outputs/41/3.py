
def solve(n, k, a):
    # Initialize two empty lists to store the students in the first and second teams
    team_1 = []
    team_2 = []
    
    # Sort the students in descending order of their programming skills
    sorted_students = sorted(a, reverse=True)
    
    # Iterate through the students and assign them to a team
    for i in range(n):
        # If the current student has a programming skill that is not already in either team, add them to the team with the highest average skill
        if sorted_students[i] not in team_1 and sorted_students[i] not in team_2:
            if len(team_1) == len(team_2):
                team_1.append(sorted_students[i])
            else:
                team_2.append(sorted_students[i])
        # If the current student has a programming skill that is already in one of the teams, add them to the other team
        else:
            if sorted_students[i] in team_1:
                team_2.append(sorted_students[i])
            else:
                team_1.append(sorted_students[i])
    
    # Return the teams as a string of 1s and 2s, with 1 representing the first team and 2 representing the second team
    return "".join([str(i + 1) for i in team_1]) + "".join([str(i + 1) for i in team_2])


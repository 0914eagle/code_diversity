
def solve(n, k, a):
    # Initialize two empty lists to store the students in the first and second team
    team_1 = []
    team_2 = []
    
    # Sort the students in descending order of their programming skills
    sorted_students = sorted(a, reverse=True)
    
    # Iterate through the students in the sorted order
    for i in range(n):
        # If the current student has a programming skill that is not already in either team, add them to the team with the lowest total programming skill
        if sorted_students[i] not in team_1 and sorted_students[i] not in team_2:
            if len(team_1) > len(team_2):
                team_2.append(sorted_students[i])
            else:
                team_1.append(sorted_students[i])
        # If the current student has a programming skill that is already in team 1, add them to team 2
        elif sorted_students[i] in team_1:
            team_2.append(sorted_students[i])
        # If the current student has a programming skill that is already in team 2, add them to team 1
        elif sorted_students[i] in team_2:
            team_1.append(sorted_students[i])
    
    # Return the teams in the form of a string of 1s and 2s, where 1 represents team 1 and 2 represents team 2
    return "".join([str(i + 1) for i in team_1]) + "".join([str(i + 1) for i in team_2])


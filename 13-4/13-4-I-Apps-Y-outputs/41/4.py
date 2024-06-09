
def solve(n, k, a):
    # Initialize two empty lists to store the students in the first and second team
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
    
    # Return the list of students in the first team
    return "".join([str(int(i in team_1)) for i in a])


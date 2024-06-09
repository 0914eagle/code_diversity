
def solve(n, k, a):
    # Initialize two empty lists to store the students in the first and second teams
    team_1 = []
    team_2 = []
    
    # Sort the students in descending order of their programming skills
    sorted_students = sorted(a, reverse=True)
    
    # Iterate through the students in the sorted order
    for i in range(n):
        # If the current student has a programming skill that is not in either team, choose them
        if sorted_students[i] not in team_1 and sorted_students[i] not in team_2:
            team_1.append(sorted_students[i])
        # If the current student has a programming skill that is in the first team, choose the next k students to their left and right
        elif sorted_students[i] in team_1:
            for j in range(i-k, i+k+1):
                if j >= 0 and j < n and sorted_students[j] not in team_1 and sorted_students[j] not in team_2:
                    team_1.append(sorted_students[j])
        # If the current student has a programming skill that is in the second team, choose the next k students to their left and right
        elif sorted_students[i] in team_2:
            for j in range(i-k, i+k+1):
                if j >= 0 and j < n and sorted_students[j] not in team_1 and sorted_students[j] not in team_2:
                    team_2.append(sorted_students[j])
    
    # Return the team assignments as a string of '1's and '2's
    return ''.join([str(1 if x in team_1 else 2) for x in a])


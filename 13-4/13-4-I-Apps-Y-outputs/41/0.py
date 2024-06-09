
def solve(n, k, a):
    # Initialize two empty lists to store the teams
    team_1 = []
    team_2 = []
    
    # Sort the students by their programming skills in descending order
    sorted_students = sorted(range(n), key=lambda i: a[i], reverse=True)
    
    # Iterate through the students and assign them to a team
    for i in range(n):
        # If the current student is not in any team, choose the student with the maximum programming skill
        if i not in team_1 and i not in team_2:
            # Add the current student to the first team
            team_1.append(sorted_students[i])
            # Add the k closest students to the left and right of the current student to the first team
            for j in range(1, k+1):
                if sorted_students[i-j] not in team_1:
                    team_1.append(sorted_students[i-j])
                if sorted_students[i+j] not in team_1:
                    team_1.append(sorted_students[i+j])
        # If the current student is already in the first team, add them to the second team
        elif i in team_1:
            team_2.append(i)
    
    # Return the teams as a string of 1s and 2s
    return "".join([str(1 if i in team_1 else 2) for i in range(n)])


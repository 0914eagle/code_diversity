
def solve(n, k, a):
    # Initialize two empty lists to store the students in the first and second teams
    team_1 = []
    team_2 = []
    
    # Sort the students in descending order of their programming skills
    sorted_students = sorted(a, reverse=True)
    
    # Iterate through the students and alternate assigning them to teams
    for i in range(n):
        if i % 2 == 0:
            # Add the current student to the first team
            team_1.append(sorted_students[i])
        else:
            # Add the current student to the second team
            team_2.append(sorted_students[i])
    
    # Return the teams in the form of a string
    return "".join([str(int(i in team_1)) for i in a])


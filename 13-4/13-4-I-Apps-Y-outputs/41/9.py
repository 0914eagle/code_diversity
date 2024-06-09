
def solve(n, k, a):
    # Initialize two empty lists to store the students in the first and second teams
    team_1 = []
    team_2 = []
    
    # Sort the students in descending order of their programming skills
    sorted_students = sorted(range(n), key=lambda i: a[i], reverse=True)
    
    # Iterate through the students in the sorted order
    for i in sorted_students:
        # If the student is not already in a team, choose them
        if i not in team_1 and i not in team_2:
            # Add the student to the first team
            team_1.append(i)
            # Find the k closest students to the left and right of the current student
            left = sorted_students[:i][-k:]
            right = sorted_students[i+1:][:k]
            # Add the closest students to the first team
            team_1.extend(left + right)
            # Remove the chosen students from the list of all students
            sorted_students = [x for x in sorted_students if x not in left + right + [i]]
    
    # The remaining students join the second team
    team_2 = sorted_students
    
    # Return the teams in the form of a string
    return "".join([str(1 if i in team_1 else 2) for i in range(n)])


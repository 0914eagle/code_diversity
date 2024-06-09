
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
            # Get the indices of the k closest students to the left and right of the current student
            left_indices = sorted_students[:i][-k:]
            right_indices = sorted_students[i+1:][:k]
            # Add the closest students to the first team
            team_1.extend(left_indices)
            team_1.extend(right_indices)
            # Remove the chosen students from the row
            sorted_students = [x for x in sorted_students if x not in left_indices and x not in right_indices and x != i]
    
    # Add the remaining students to the second team
    team_2.extend(sorted_students)
    
    # Return the teams as a string of 1s and 2s
    return "".join([str(1 if i in team_1 else 2) for i in range(n)])


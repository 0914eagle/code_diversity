
def find_two_holes(n, p):
    # Initialize a dictionary to store the number of holes for each student
    holes = {i: 0 for i in range(1, n + 1)}
    
    # Iterate through the array of reported students
    for i in range(n):
        # If the current student has already received a hole, skip them
        if holes[i] == 1:
            continue
        # Find the next student in the chain who has not received a hole yet
        next_student = i
        while holes[next_student] == 0:
            holes[next_student] = 1
            next_student = p[next_student]
        # If the next student is the first student, they receive a second hole
        if next_student == 1:
            holes[next_student] = 2
    
    # Return the dictionary of holes for each student
    return holes



def solve(n, p):
    # Initialize a dictionary to store the number of holes for each student
    holes = {i: 0 for i in range(1, n + 1)}
    
    # Iterate through the list of reported students
    for i in range(n):
        # If the current student has not been reported yet, mark him as reported
        if holes[i] == 0:
            holes[i] = 1
            # Update the number of holes for the student who reported the current student
            holes[p[i]] += 1
    
    # Return a list of students who will receive two holes in their badges
    return [i for i in range(1, n + 1) if holes[i] == 2]



def solve(n, p):
    # Initialize a dictionary to store the number of holes for each student
    holes = {i: 0 for i in range(1, n + 1)}
    
    # Iterate through the list of reported students
    for i in range(n):
        # If the current student has already received a hole, skip them
        if holes[i] == 1:
            continue
        # If the current student has not received a hole, mark their reported student as having a hole
        holes[p[i - 1]] = 1
    
    # Return the student with two holes in their badge
    return [hole for hole in holes if holes[hole] == 2][0]


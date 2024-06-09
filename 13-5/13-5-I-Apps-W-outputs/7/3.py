
def get_max_strength(n, m, p, c, d, k):
    # Initialize the team strength for each day
    team_strength = [0] * d
    
    # Initialize the number of students in each club
    num_students = [0] * m
    
    # Initialize the potential of each student
    student_potential = [0] * n
    
    # Initialize the club of each student
    student_club = [0] * n
    
    # Fill in the potential and club of each student
    for i in range(n):
        student_potential[i] = p[i]
        student_club[i] = c[i]
        num_students[c[i] - 1] += 1
    
    # Fill in the team strength for each day
    for i in range(d):
        # Find the student who left their club on the current day
        student_left = k[i] - 1
        
        # Update the number of students in the club of the student who left
        num_students[student_club[student_left] - 1] -= 1
        
        # Update the team strength for the current day
        team_strength[i] = get_mex(student_potential, student_club, num_students, student_left)
    
    return team_strength

def get_mex(student_potential, student_club, num_students, student_left):
    # Initialize the mex
    mex = 0
    
    # Iterate through the students in the club of the student who left
    for i in range(num_students[student_club[student_left] - 1]):
        # Find the student with the maximum potential in the club
        max_potential = 0
        for j in range(num_students[student_club[student_left] - 1]):
            if student_potential[i + j] > max_potential:
                max_potential = student_potential[i + j]
        
        # Update the mex
        if max_potential > mex:
            mex = max_potential
    
    return mex

if __name__ == '__main__':
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = int(input())
    k = list(map(int, input().split()))
    team_strength = get_max_strength(n, m, p, c, d, k)
    for i in range(d):
        print(team_strength[i])


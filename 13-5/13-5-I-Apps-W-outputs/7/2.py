
def get_maximum_strength(n, m, p, c, d, k):
    # Initialize a dictionary to store the strength of each club
    club_strength = {}
    for i in range(m):
        club_strength[i] = 0
    
    # Initialize a set to store the students who have left their club
    left_students = set()
    
    # Loop through each day
    for i in range(d):
        # Get the index of the student who left their club on the current day
        k_i = k[i]
        
        # Add the student to the set of left students
        left_students.add(k_i)
        
        # Loop through each club
        for j in range(m):
            # Get the potential of the students in the current club
            club_potential = [p[student] for student in range(n) if c[student] == j+1 and student not in left_students]
            
            # Update the strength of the club
            club_strength[j] = max(club_strength[j], mex(club_potential))
    
    # Return the maximum strength of all clubs
    return max(club_strength.values())

def mex(S):
    # Find the smallest non-negative integer that is not present in S
    for i in range(len(S)):
        if i not in S:
            return i
    return 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = int(input())
    k = list(map(int, input().split()))
    print(get_maximum_strength(n, m, p, c, d, k))


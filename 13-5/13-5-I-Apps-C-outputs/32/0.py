
def get_optimal_solution(students, bugs, passes):
    # Sort the students and bugs by their levels and complexities respectively
    students = sorted(students, key=lambda x: x[1])
    bugs = sorted(bugs, key=lambda x: x[0])
    
    # Initialize the solution
    solution = []
    days = 0
    
    # Iterate through the students and bugs
    for student, ability in students:
        for bug, complexity in bugs:
            # Check if the student can fix the bug
            if ability >= complexity:
                # Add the student to the solution
                solution.append(student)
                # Remove the bug from the list of bugs
                bugs.remove(bug)
                # Increment the number of days
                days += 1
                # Break out of the inner loop
                break
    
    # Check if all the bugs have been fixed
    if len(bugs) == 0:
        return days, solution
    else:
        return -1, []

def main():
    # Read the input
    n, m, s = map(int, input().split())
    students = [tuple(map(int, input().split())) for _ in range(n)]
    bugs = [tuple(map(int, input().split())) for _ in range(m)]
    
    # Get the optimal solution
    days, solution = get_optimal_solution(students, bugs, s)
    
    # Check if an optimal solution exists
    if days == -1:
        print("NO")
    else:
        print("YES")
        print(*solution)

if __name__ == '__main__':
    main()


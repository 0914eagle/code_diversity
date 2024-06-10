
def get_optimal_solution(n, m, s, a, b, c):
    # Sort the bugs and students by their complexities and abilities
    sorted_bugs = sorted(range(m), key=lambda i: a[i])
    sorted_students = sorted(range(n), key=lambda i: b[i])
    
    # Initialize the variables for the greedy algorithm
    current_day = 0
    passes_given = 0
    student_choices = [-1] * m
    bug_assignees = [-1] * m
    
    # Iterate through the sorted bugs and students
    for i in range(m):
        for j in range(n):
            # Check if the student can fix the bug and if the passes given do not exceed the maximum
            if b[sorted_students[j]] >= a[sorted_bugs[i]] and passes_given + c[sorted_students[j]] <= s:
                # Assign the bug to the student and update the variables
                student_choices[sorted_bugs[i]] = sorted_students[j]
                bug_assignees[sorted_bugs[i]] = current_day
                passes_given += c[sorted_students[j]]
                break
        current_day += 1
    
    # Check if all the bugs were assigned
    if -1 in student_choices:
        return "NO"
    
    # Return the optimal solution
    return "YES\n" + " ".join(str(i+1) for i in student_choices)

def main():
    n, m, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(get_optimal_solution(n, m, s, a, b, c))

if __name__ == '__main__':
    main()


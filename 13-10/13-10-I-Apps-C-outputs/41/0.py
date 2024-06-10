
def get_optimal_solution(n, m, s, a, b, c):
    # Sort the bugs by complexity in descending order
    sorted_bugs = sorted(range(m), key=lambda i: a[i], reverse=True)
    
    # Initialize the number of passes given to each student to 0
    passes_given = [0] * n
    
    # Initialize the number of days spent on each bug to 0
    days_spent = [0] * m
    
    # Initialize the student assigned to each bug to -1 (no student assigned yet)
    student_assigned = [-1] * m
    
    # Loop through the bugs in descending order of complexity
    for i in sorted_bugs:
        # Find the student with the highest level of ability who has not yet been assigned a bug
        student = -1
        for j in range(n):
            if passes_given[j] + b[j] >= a[i] and student_assigned[i] == -1:
                student = j
                break
        
        # If no student has the required level of ability, the university cannot correct the bug
        if student == -1:
            return "NO"
        
        # Assign the bug to the student
        student_assigned[i] = student
        
        # Increment the number of passes given to the student
        passes_given[student] += b[student]
        
        # Increment the number of days spent on the bug
        days_spent[i] += 1
    
    # If the total number of passes exceeds the maximum allowed by the university, return "NO"
    if sum(passes_given) > s:
        return "NO"
    
    # Otherwise, return "YES" and the optimal solution
    return "YES", student_assigned

def main():
    n, m, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(get_optimal_solution(n, m, s, a, b, c))

if __name__ == '__main__':
    main()


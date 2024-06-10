
def get_optimal_solution(n, m, s, bugs, students):
    # Sort the students by their ability levels in descending order
    students = sorted(students, reverse=True)
    # Initialize the variables to keep track of the passes and days needed
    passes = 0
    days = 0
    # Create a list to store the student-bug assignments
    assignments = []
    # Loop through the bugs and students
    for i in range(m):
        for j in range(n):
            # Check if the student can fix the bug
            if students[j] >= bugs[i]:
                # Add the student-bug assignment to the list
                assignments.append([j, i])
                # Increment the passes and days needed
                passes += 1
                days += 1
                # Check if the passes exceed the maximum allowed
                if passes > s:
                    return "NO"
                # Break out of the inner loop
                break
    # Check if all the bugs are fixed
    if len(assignments) < m:
        return "NO"
    # Sort the assignments by the day needed in ascending order
    assignments = sorted(assignments, key=lambda x: x[1])
    # Return the optimal solution
    return "YES\n" + " ".join(str(x[0] + 1) for x in assignments)

def main():
    # Read the input
    n, m, s = map(int, input().split())
    bugs = list(map(int, input().split()))
    students = list(map(int, input().split()))
    # Call the function to get the optimal solution
    solution = get_optimal_solution(n, m, s, bugs, students)
    # Print the solution
    print(solution)

if __name__ == '__main__':
    main()


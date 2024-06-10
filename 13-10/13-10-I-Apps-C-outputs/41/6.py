
def get_optimal_student_schedule(student_abilities, bug_complexities, passes_required, passes_given):
    # Sort the students and bugs in descending order
    student_abilities = sorted(student_abilities, reverse=True)
    bug_complexities = sorted(bug_complexities, reverse=True)
    
    # Initialize the schedule and passes variables
    schedule = []
    passes = 0
    
    # Loop through the students and bugs
    for student, bug in zip(student_abilities, bug_complexities):
        # If the student's ability is greater than or equal to the bug's complexity, and the passes required is less than or equal to the passes given, add the student to the schedule and increment the passes variable
        if student >= bug and passes < passes_required:
            schedule.append(student)
            passes += 1
    
    # If the passes required is greater than the passes given, return "NO"
    if passes > passes_given:
        return "NO"
    
    # Otherwise, return "YES" and the schedule
    return "YES", schedule

def main():
    # Read the input
    n, m, s = map(int, input().split())
    student_abilities = list(map(int, input().split()))
    bug_complexities = list(map(int, input().split()))
    passes_required = list(map(int, input().split()))
    
    # Call the function to get the optimal student schedule
    result = get_optimal_student_schedule(student_abilities, bug_complexities, passes_required, s)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()


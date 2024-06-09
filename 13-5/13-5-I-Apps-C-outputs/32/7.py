
def get_optimal_schedule(students, bugs, passes):
    # Sort the students by their ability level in descending order
    students.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the schedule as a list of tuples (student_id, bug_id)
    schedule = []
    
    # Iterate through the bugs and assign them to the students
    for bug in bugs:
        # Find the student with the highest ability level that can fix the current bug
        for student in students:
            if student[1] >= bug:
                schedule.append((student[0], bug))
                break
    
    # Calculate the total number of passes required by the students
    total_passes = sum([students[schedule[i][0]][2] for i in range(len(schedule))])
    
    # Check if the total number of passes does not exceed the maximum allowed by the university
    if total_passes <= passes:
        return schedule
    else:
        return None

def main():
    n, m, s = map(int, input().split())
    bugs = list(map(int, input().split()))
    students = []
    for i in range(n):
        students.append(list(map(int, input().split())))
    
    schedule = get_optimal_schedule(students, bugs, s)
    
    if schedule is None:
        print("NO")
    else:
        print("YES")
        for student, bug in schedule:
            print(student, end=" ")
        print()

if __name__ == '__main__':
    main()


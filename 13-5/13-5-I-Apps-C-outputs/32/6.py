
def get_optimal_students(n, m, s, a, b, c):
    # Sort the bugs by complexity in ascending order
    sorted_bugs = sorted(range(m), key=lambda i: a[i])

    # Initialize the students and their passes
    students = [Student(i, b[i], c[i]) for i in range(n)]

    # Initialize the schedule and the number of passes used
    schedule = [0] * m
    passes_used = 0

    # Iterate through the bugs and assign them to the students
    for i in sorted_bugs:
        # Find the student with the highest ability level that can fix the current bug
        student = max(students, key=lambda s: s.ability_level)

        # If the student can't fix the bug, return "NO"
        if student.ability_level < a[i]:
            return "NO"

        # Assign the bug to the student and update the schedule and passes used
        student.fix_bug(i)
        schedule[i] = student.id
        passes_used += student.passes_needed

        # If the passes used exceed the maximum number of passes, return "NO"
        if passes_used > s:
            return "NO"

    # If all bugs are fixed, return "YES" and the schedule
    return "YES", schedule

class Student:
    def __init__(self, id, ability_level, passes_needed):
        self.id = id
        self.ability_level = ability_level
        self.passes_needed = passes_needed
        self.bugs_fixed = 0

    def fix_bug(self, bug_id):
        self.bugs_fixed += 1

if __name__ == '__main__':
    n, m, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    result = get_optimal_students(n, m, s, a, b, c)
    print(result[0])
    if result[0] == "YES":
        print(*result[1])


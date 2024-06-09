
def get_optimal_students(n, m, s, a, b, c):
    # Sort the bugs by complexity in ascending order
    sorted_bugs = sorted(enumerate(a), key=lambda x: x[1])

    # Sort the students by their ability level in descending order
    sorted_students = sorted(enumerate(b), key=lambda x: x[1], reverse=True)

    # Initialize the passes given to each student
    passes_given = [0] * n

    # Initialize the list of students who will fix each bug
    bug_fixers = [0] * m

    # Loop through the bugs and assign them to the students
    for i, (j, complexity) in enumerate(sorted_bugs):
        # Find the student with the highest ability level who can fix the current bug
        for k, (student, ability) in enumerate(sorted_students):
            if ability >= complexity:
                # Assign the current bug to the current student
                bug_fixers[j] = student
                # Increment the passes given to the current student
                passes_given[student] += c[student]
                break

        # If the passes given exceed the maximum passes allowed, return "NO"
        if sum(passes_given) > s:
            return "NO"

    # If all bugs have been fixed, return "YES" and the list of students who will fix each bug
    return "YES", bug_fixers

def main():
    n, m, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    result = get_optimal_students(n, m, s, a, b, c)
    print(result[0])
    if result[0] == "YES":
        print(*result[1])

if __name__ == '__main__':
    main()


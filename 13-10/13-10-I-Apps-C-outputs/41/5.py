
def get_optimal_solution(n, m, s, a, b, c):
    # Sort the bugs by complexity in descending order
    sorted_bugs = sorted(range(m), key=lambda i: a[i])

    # Initialize the variables
    passes_given = 0
    student_map = [-1] * m
    days_taken = 0

    # Iterate through the bugs
    for i in sorted_bugs:
        # Find the student with the highest level of ability
        max_level = -1
        for j in range(n):
            if b[j] > max_level:
                max_level = b[j]
                best_student = j

        # Check if the student is able to fix the bug
        if max_level < a[i]:
            return "NO"

        # Give the student the pass
        passes_given += c[best_student]
        student_map[i] = best_student
        days_taken += 1

        # Check if the passes given exceed the maximum
        if passes_given > s:
            return "NO"

    return "YES\n" + " ".join(map(str, student_map))

def main():
    n, m, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(get_optimal_solution(n, m, s, a, b, c))

if __name__ == '__main__':
    main()


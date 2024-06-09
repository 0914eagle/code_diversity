
def get_optimal_solution(n, m, s, a, b, c):
    # Sort the bugs by complexity in descending order
    sorted_bugs = sorted(range(m), key=lambda i: a[i], reverse=True)

    # Initialize the students' passes and the number of days needed to fix the bugs
    passes = [0] * n
    days = 0

    # Iterate through the bugs and assign them to the students
    for i in sorted_bugs:
        # Find the student with the highest level of ability who can fix the current bug
        student = max(range(n), key=lambda j: b[j] - a[i])

        # Increment the student's passes and the number of days needed to fix the bug
        passes[student] += 1
        days += 1

        # If the total number of passes exceeds the maximum allowed by the university, return "NO"
        if sum(passes) > s:
            return "NO"

    # If all bugs are fixed, return "YES" and the schedule of work
    return "YES\n" + " ".join(map(str, passes))

def main():
    n, m, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(get_optimal_solution(n, m, s, a, b, c))

if __name__ == '__main__':
    main()


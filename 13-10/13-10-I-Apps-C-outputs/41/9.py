
def get_optimal_solution(n, m, s, a, b, c):
    # Sort the bugs by complexity in descending order
    sorted_bugs = sorted(range(m), key=lambda i: a[i])

    # Initialize the solution
    solution = [-1] * m
    passes = 0

    # Iterate through the bugs
    for i in range(m):
        # Find the student with the highest level of ability
        student = max(range(n), key=lambda i: b[i])

        # If the student is not able to fix the current bug, skip it
        if b[student] < a[sorted_bugs[i]]:
            continue

        # Assign the current bug to the student
        solution[sorted_bugs[i]] = student

        # Update the total number of passes
        passes += c[student]

        # If the total number of passes exceeds the limit, return "NO"
        if passes > s:
            return "NO"

    # Return the optimal solution
    return "YES\n" + " ".join(map(str, solution))

def main():
    n, m, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(get_optimal_solution(n, m, s, a, b, c))

if __name__ == '__main__':
    main()


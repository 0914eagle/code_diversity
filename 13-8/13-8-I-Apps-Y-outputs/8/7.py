
def is_valid_solution(solution, a, n, m, segments, umbrellas):
    # Check if the solution is valid
    if solution[0] != 0 or solution[-1] != a:
        return False
    for i in range(1, len(solution)):
        if solution[i] <= solution[i-1]:
            return False
    for i in range(n):
        if solution[segments[i][0]] != solution[segments[i][1]]:
            return False
    for i in range(m):
        if solution[umbrellas[i][0]] != solution[umbrellas[i][1]]:
            return False
    return True

def get_fatigue(solution, umbrellas):
    # Calculate the total fatigue of the solution
    fatigue = 0
    for i in range(len(solution)-1):
        fatigue += sum(umbrellas[j][1] for j in range(len(umbrellas)) if solution[j] == solution[i+1])
    return fatigue

def solve(a, n, m, segments, umbrellas):
    # Initialize the solution with all umbrellas at point 0
    solution = [0 for _ in range(a+1)]
    for i in range(m):
        solution[umbrellas[i][0]] = umbrellas[i][1]
    # Iterate through each segment and find the best umbrella to pick up
    for i in range(n):
        current_segment = segments[i]
        current_fatigue = get_fatigue(solution, umbrellas)
        best_fatigue = current_fatigue
        best_umbrella = -1
        for j in range(m):
            if solution[umbrellas[j][0]] == 0:
                continue
            solution[umbrellas[j][0]] = 0
            new_fatigue = get_fatigue(solution, umbrellas)
            if new_fatigue < best_fatigue:
                best_fatigue = new_fatigue
                best_umbrella = j
        if best_umbrella == -1:
            return -1
        solution[current_segment[1]] = umbrellas[best_umbrella][1]
    # Check if the solution is valid
    if not is_valid_solution(solution, a, n, m, segments, umbrellas):
        return -1
    # Return the minimum fatigue of the solution
    return get_fatigue(solution, umbrellas)

def main():
    a, n, m = map(int, input().split())
    segments = [tuple(map(int, input().split())) for _ in range(n)]
    umbrellas = [tuple(map(int, input().split())) for _ in range(m)]
    print(solve(a, n, m, segments, umbrellas))

if __name__ == '__main__':
    main()


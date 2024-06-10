
def get_max_score(n, T, a, t):
    # Sort the problems by their time required in descending order
    sorted_problems = sorted(range(n), key=lambda i: t[i])

    # Initialize the maximum score and the chosen problems
    max_score = 0
    chosen_problems = []

    # Loop through the problems and choose the ones that can be solved within the time limit
    for i in sorted_problems:
        if t[i] <= T:
            max_score += 1
            chosen_problems.append(i)
            T -= t[i]

    return max_score, chosen_problems

def main():
    n, T = map(int, input().split())
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))
    max_score, chosen_problems = get_max_score(n, T, a, t)
    print(max_score)
    print(len(chosen_problems))
    print(*chosen_problems)

if __name__ == '__main__':
    main()


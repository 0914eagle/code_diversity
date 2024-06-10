
def get_problemset(n, k, teams):
    # Initialize a set to store the selected problems
    selected_problems = set()

    # Iterate over the teams
    for team in teams:
        # Get the problems known by the current team
        known_problems = set(i for i, problem in enumerate(team) if problem == 1)

        # If the current team knows at least half of the selected problems, add the problems known by the current team to the selected problems set
        if len(known_problems & selected_problems) >= len(selected_problems) // 2:
            selected_problems |= known_problems

    # If the selected problems set is not empty and it contains at least half of the total number of problems, return "YES"
    return "YES" if selected_problems and len(selected_problems) >= n // 2 else "NO"

def main():
    n, k = map(int, input().split())
    teams = [list(map(int, input().split())) for _ in range(n)]
    print(get_problemset(n, k, teams))

if __name__ == '__main__':
    main()


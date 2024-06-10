
def is_interesting_problemset(problems, teams):
    # Initialize variables
    selected_problems = set()
    team_problems = [set(team) for team in teams]

    # Iterate through the problems
    for i in range(len(problems)):
        # If the problem is not already selected, add it to the selected problems
        if i not in selected_problems:
            selected_problems.add(i)
            # Check if any team knows more than half of the selected problems
            for team in team_problems:
                if len(selected_problems.intersection(team)) > len(selected_problems) // 2:
                    return False

    return True

def main():
    # Read the input
    n, k = map(int, input().split())
    teams = []
    for _ in range(n):
        teams.append(list(map(int, input().split())))

    # Call the is_interesting_problemset function
    result = is_interesting_problemset(range(n), teams)

    # Print the result
    print("YES") if result else print("NO")

if __name__ == '__main__':
    main()


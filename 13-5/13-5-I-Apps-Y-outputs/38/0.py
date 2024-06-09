
def get_teams(n, a):
    # Sort the array in ascending order
    a.sort()
    # Initialize the teams array
    teams = []
    # Initialize the current team with the first three elements of the array
    current_team = a[:3]
    # Iterate over the rest of the array
    for i in range(3, n):
        # If the current team has a diversity that is less than or equal to the diversity of the current element, add the element to the current team
        if get_diversity(current_team) <= get_diversity([*current_team, a[i]]):
            current_team.append(a[i])
        # Otherwise, create a new team with the current element
        else:
            teams.append(current_team)
            current_team = [a[i]]
    # Add the last team
    teams.append(current_team)
    return teams

def get_diversity(team):
    return max(team) - min(team)

def get_total_diversity(teams):
    return sum([get_diversity(team) for team in teams])

def main():
    n = int(input())
    a = list(map(int, input().split()))
    teams = get_teams(n, a)
    print(get_total_diversity(teams))
    print(*[teams.index(team) + 1 for team in teams])

if __name__ == '__main__':
    main()


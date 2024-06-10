
def read_input():
    n, k = map(int, input().split())
    teams = []
    for _ in range(n):
        teams.append(list(map(int, input().split())))
    return n, k, teams

def is_interesting(teams):
    # Calculate the number of problems each team knows
    team_knowledge = [sum(team) for team in teams]
    
    # Calculate the number of problems each team needs to know
    team_needs = [int(team_knowledge[i] < k/2) for i in range(len(teams))]
    
    # Check if any team needs to know more problems than it currently knows
    if any(team_needs):
        return False
    
    return True

def solve():
    n, k, teams = read_input()
    if is_interesting(teams):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()


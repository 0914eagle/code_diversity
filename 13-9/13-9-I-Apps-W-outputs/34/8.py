
def get_team_strength(team_strengths):
    # Sort the team strengths in descending order
    team_strengths.sort(reverse=True)
    # Initialize the teammate array
    teammates = [0] * len(team_strengths)
    # Loop through the team strengths and find the teammate for each person
    for i in range(len(team_strengths)):
        # Find the best teammate for the current person
        best_teammate = 0
        for j in range(1, len(team_strengths)):
            if team_strengths[i] > team_strengths[j] and teammates[j] == 0:
                best_teammate = j
                break
        # Update the teammate array
        teammates[i] = best_teammate + 1
    return teammates

def main():
    n = int(input())
    team_strengths = []
    for i in range(n):
        team_strengths.append(list(map(int, input().split())))
    teammates = get_team_strength(team_strengths)
    print(*teammates)

if __name__ == '__main__':
    main()


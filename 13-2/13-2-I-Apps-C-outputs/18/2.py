
n, k = map(int, input().split())
teams = [list(map(int, input().split())) for _ in range(n)]

# Check if any team knows all problems
if any(all(team) for team in teams):
    print("NO")
    exit()

# Check if any team knows at most half of the problems
if any(sum(team) > n // 2 for team in teams):
    print("NO")
    exit()

# Check if any two teams know the same problem
for i in range(n):
    for j in range(i + 1, n):
        if teams[i][j] == 1 and teams[j][i] == 1:
            print("NO")
            exit()

print("YES")



def solve(n, a):
    # Sort the array of skills in ascending order
    a.sort()
    # Initialize the minimum number of teams as 0
    min_teams = 0
    # Iterate through the array of skills
    for i in range(n-1):
        # Check if the difference between the current skill and the next skill is 1
        if a[i+1] - a[i] == 1:
            # Increment the minimum number of teams
            min_teams += 1
    # Return the minimum number of teams
    return min_teams

q = int(input())
for i in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))


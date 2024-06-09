
def get_min_teams(a):
    # Sort the array in ascending order
    a.sort()
    # Initialize the minimum number of teams as 1
    min_teams = 1
    # Iterate over the array
    for i in range(len(a)):
        # Check if the current element is within the range of the previous element plus or minus 1
        if a[i] - a[i-1] in [1, -1]:
            # If it is, increment the minimum number of teams
            min_teams += 1
    return min_teams

q = int(input())
for i in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    print(get_min_teams(a))


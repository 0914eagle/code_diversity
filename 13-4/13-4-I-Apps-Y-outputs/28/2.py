
def get_min_teams(a):
    # Sort the array in ascending order
    a.sort()
    # Initialize the minimum number of teams as 1
    min_teams = 1
    # Loop through the array
    for i in range(len(a)-1):
        # Check if the difference between the current element and the next element is 1
        if a[i+1] - a[i] == 1:
            # Increment the minimum number of teams
            min_teams += 1
    return min_teams

q = int(input())
for i in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    print(get_min_teams(a))


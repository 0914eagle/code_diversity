
n = int(input())
guardposts = []
for i in range(4):
    guardposts.append([int(x) for x in input().split()])

# Use a dictionary to keep track of the minimum cost of the gifts for each guardpost
min_cost = {}
for i in range(4):
    min_cost[i+1] = [guardposts[i][0], guardposts[i][2]]

# Use a dictionary to keep track of the total cost of the gifts for each guardpost
total_cost = {}
for i in range(4):
    total_cost[i+1] = 0

# Iterate through the guardposts and calculate the total cost of the gifts for each one
for i in range(4):
    for j in range(2):
        total_cost[i+1] += min(min_cost[i+1][j], n)

# Find the guardpost with the minimum total cost that is less than or equal to the given amount
min_total_cost = float('inf')
min_guardpost = -1
for i in range(4):
    if total_cost[i+1] <= n and total_cost[i+1] < min_total_cost:
        min_total_cost = total_cost[i+1]
        min_guardpost = i+1

# Print the result
if min_guardpost != -1:
    print(min_guardpost, min(min_cost[min_guardpost][0], n), min(min_cost[min_guardpost][1], n))
else:
    print(-1)


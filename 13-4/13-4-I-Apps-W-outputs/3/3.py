
n = int(input())
guardposts = []
for i in range(4):
    guardposts.append(list(map(int, input().split())))

# Find the guardpost with the minimum total cost
min_cost = float('inf')
min_post = -1
for i in range(4):
    cost = sum([max(n//2, guardposts[i][0]), max(n//2, guardposts[i][2])])
    if cost < min_cost:
        min_cost = cost
        min_post = i+1

if min_post == -1:
    print(-1)
else:
    print(min_post, n//2, n//2)


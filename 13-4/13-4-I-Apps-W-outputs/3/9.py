
n = int(input())
guard_posts = []
for i in range(4):
    guard_post = list(map(int, input().split()))
    guard_posts.append(guard_post)

# Find the guard post with the minimum total cost
min_cost = float('inf')
min_post = -1
for i in range(4):
    cost = guard_posts[i][0] + guard_posts[i][1]
    if cost < min_cost:
        min_cost = cost
        min_post = i + 1

# Check if the total cost is less than or equal to n
if min_cost <= n:
    print(min_post, guard_posts[min_post][0], guard_posts[min_post][1])
else:
    print(-1)


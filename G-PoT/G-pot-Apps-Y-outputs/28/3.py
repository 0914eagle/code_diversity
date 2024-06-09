
n, k = map(int, input().split())
ratings = list(map(int, input().split()))

rating_indices = {}
for i, rating in enumerate(ratings):
    if rating not in rating_indices:
        rating_indices[rating] = []
    rating_indices[rating].append(i+1)

if len(rating_indices) < k:
    print("NO")
else:
    print("YES")
    team_indices = []
    for indices in rating_indices.values():
        team_indices.extend(indices[:k])
        if len(team_indices) >= k:
            break
    print(*team_indices[:k])

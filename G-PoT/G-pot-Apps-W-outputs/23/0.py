
K = int(input())
ranks = list(map(int, input().split()))

max_rank = max(ranks)
min_rank = min(ranks)

missing_contestants = 0
for i in range(min_rank, max_rank):
    if i not in ranks:
        missing_contestants += 1

print(missing_contestants)

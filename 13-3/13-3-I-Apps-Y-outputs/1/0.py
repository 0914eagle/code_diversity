
import sys

n, m = map(int, input().split())
votes = list(map(int, input().split()))

total_votes = sum(votes)
min_votes = total_votes // 4 * m

selected_items = []
for vote in votes:
    if vote >= min_votes:
        selected_items.append(vote)

if len(selected_items) == m:
    print("Yes")
else:
    print("No")


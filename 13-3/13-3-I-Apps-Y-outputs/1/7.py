
import sys

n, m = map(int, input().split())
votes = list(map(int, input().split()))

# Calculate the total number of votes
total_votes = sum(votes)

# Sort the votes in descending order
votes.sort(reverse=True)

# Check if we can select M popular items
if m <= n and votes[m-1] >= total_votes/4:
    print("Yes")
else:
    print("No")


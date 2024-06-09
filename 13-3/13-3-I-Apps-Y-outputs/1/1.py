
import sys

n, m = map(int, input().split())
votes = list(map(int, input().split()))

# Calculate the total number of votes
total_votes = sum(votes)

# Calculate the minimum number of votes required for an item to be considered popular
min_votes = total_votes / (4 * m)

# Find the M most popular items
popular_items = sorted(votes, reverse=True)[:m]

# Check if the minimum number of votes is met for all popular items
if all(item >= min_votes for item in popular_items):
    print("Yes")
else:
    print("No")


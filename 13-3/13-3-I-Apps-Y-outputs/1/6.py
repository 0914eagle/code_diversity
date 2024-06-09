
import sys

n, m = map(int, input().split())
votes = list(map(int, input().split()))

# Sort the votes in descending order
votes.sort(reverse=True)

# Calculate the minimum number of votes required for an item to be considered popular
min_votes = int(n / (4 * m)) + 1

# Initialize a counter to keep track of the number of popular items selected
popular_items = 0

# Iterate through the sorted votes and select the items that have at least the minimum number of votes
for vote in votes:
    if vote >= min_votes:
        popular_items += 1
        if popular_items == m:
            print("Yes")
            break
else:
    print("No")


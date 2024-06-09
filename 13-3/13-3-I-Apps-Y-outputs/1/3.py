
import sys

n, m = map(int, input().split())
votes = list(map(int, input().split()))

# Sort the votes in descending order
votes.sort(reverse=True)

# Calculate the minimum number of votes required to select M popular items
min_votes = int(len(votes) / (4 * m))

# Initialize a counter for the number of popular items selected
count = 0

# Iterate through the sorted votes and select the items with at least min_votes
for vote in votes:
    if vote >= min_votes:
        count += 1
        if count == m:
            print("Yes")
            break

# If we reach the end of the loop and M popular items have not been selected, print No
else:
    print("No")


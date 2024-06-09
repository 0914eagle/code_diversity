
import sys

n, m = map(int, input().split())
votes = list(map(int, input().split()))

# Sort the votes in descending order
votes.sort(reverse=True)

# Calculate the minimum number of votes required for an item to be selected
min_votes = int(len(votes) / (4 * m))

# Initialize a counter for the number of selected items
selected = 0

# Iterate through the votes and select the items that meet the minimum vote requirement
for vote in votes:
    if vote >= min_votes:
        selected += 1
        if selected == m:
            break

# Check if M popular items can be selected
if selected == m:
    print("Yes")
else:
    print("No")


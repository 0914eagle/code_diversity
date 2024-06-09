
import sys

n, m = map(int, input().split())
votes = list(map(int, input().split()))

# Sort the votes in descending order
votes.sort(reverse=True)

# Calculate the minimum number of votes required for an item to be considered popular
min_votes = int(n / (4 * m)) + 1

# Initialize a counter for the number of popular items
popular_items = 0

# Iterate through the votes and check if an item is popular
for vote in votes:
    if vote >= min_votes:
        popular_items += 1

# Check if M popular items can be selected
if popular_items >= m:
    print("Yes")
else:
    print("No")


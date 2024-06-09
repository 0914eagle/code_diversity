
import sys

n, m = map(int, input().split())
votes = list(map(int, input().split()))

# Calculate the total number of votes
total_votes = sum(votes)

# Sort the votes in descending order
votes.sort(reverse=True)

# Check if we can select M popular items
if m > n:
    print("No")
    sys.exit()

# Check if the most popular item has at least 1/4 of the total votes
if votes[0] < total_votes / 4:
    print("No")
    sys.exit()

# Select the M popular items
selected_items = votes[:m]

# Check if the sum of the votes of the selected items is at least 1/4 of the total votes
if sum(selected_items) < total_votes / 4:
    print("No")
else:
    print("Yes")


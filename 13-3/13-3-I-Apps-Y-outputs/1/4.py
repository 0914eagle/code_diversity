
import sys

n, m = map(int, input().split())
votes = list(map(int, input().split()))

# Check if the number of votes is greater than or equal to 1/4M
if sum(votes) >= n // 4:
    # Sort the votes in descending order
    votes.sort(reverse=True)
    # Initialize a counter for the number of selected items
    count = 0
    # Iterate through the votes and select the items with the highest number of votes
    for vote in votes:
        if vote > 0:
            count += 1
            vote -= 1
        if count == m:
            break
    # Check if we have selected M items
    if count == m:
        print("Yes")
    else:
        print("No")
else:
    print("No")


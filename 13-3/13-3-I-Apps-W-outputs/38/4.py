
n, m = map(int, input().split())

# Initialize the number of moves to 0
moves = 0

# Loop through the possible number of moves
for i in range(1, n + 1):
    # Check if the current number of moves is a multiple of m
    if i % m == 0:
        # If it is, break the loop and print the number of moves
        moves = i
        break

# If no multiple of m was found, print -1
if moves == 0:
    print(-1)
else:
    print(moves)


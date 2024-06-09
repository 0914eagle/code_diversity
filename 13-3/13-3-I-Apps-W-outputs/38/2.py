
n, m = map(int, input().split())

# Initialize the minimum number of moves to -1
min_moves = -1

# Iterate through all possible sequences of steps
for i in range(1, n + 1):
    # Check if the current sequence of steps is a multiple of m
    if i % m == 0:
        # If it is, update the minimum number of moves
        min_moves = i
        break

print(min_moves)


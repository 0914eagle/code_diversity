
# Read input
A, B = map(int, input().split())

# Determine the outcome of the game
if A == 1:
    A = 14
if B == 1:
    B = 14

if A > B:
    print("Alice")
elif A < B:
    print("Bob")
else:
    print("Draw")

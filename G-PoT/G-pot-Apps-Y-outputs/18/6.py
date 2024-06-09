
# Read input
A, B = map(int, input().split())

# Determine the outcome of the game
if A == 1:
    if B == 1:
        print("Draw")
    else:
        print("Alice")
elif B == 1:
    print("Bob")
elif A > B:
    print("Alice")
elif A < B:
    print("Bob")
else:
    print("Draw")


def whose_turn_to_serve(N, P, Q):
    total_points = P + Q
    rounds_played = total_points // N
    if rounds_played % 2 == 0:
        return "paul"
    else:
        return "opponent"

# Input
N, P, Q = map(int, input().split())

# Output
print(whose_turn_to_serve(N, P, Q))

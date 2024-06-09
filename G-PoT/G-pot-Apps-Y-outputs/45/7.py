
def whose_turn_to_serve(N, P, Q):
    total_points = P + Q
    if total_points // N % 2 == 0:
        return "paul"
    else:
        return "opponent"

# Input
N, P, Q = map(int, input().split())

# Output
print(whose_turn_to_serve(N, P, Q))

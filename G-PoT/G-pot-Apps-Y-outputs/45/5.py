
def whose_turn_to_serve(N, P, Q):
    total_points = P + Q
    if total_points // N % 2 == 0:
        return "paul"
    else:
        return "opponent"

# Read input values
N, P, Q = map(int, input().split())

# Call the function and print the output
print(whose_turn_to_serve(N, P, Q))

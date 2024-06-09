
def solve(A, B, C, D, P, M, G):
    # Calculate the minute during which the dogs are aggressive
    aggressive_minute_postman = (P + A) % (A + B)
    aggressive_minute_milkman = (M + C) % (C + D)
    aggressive_minute_garbage_man = (G + A) % (A + B)

    # Check which dogs attack each of the heroes
    if aggressive_minute_postman == aggressive_minute_milkman == aggressive_minute_garbage_man:
        return "both"
    elif aggressive_minute_postman == aggressive_minute_milkman or aggressive_minute_postman == aggressive_minute_garbage_man or aggressive_minute_milkman == aggressive_minute_garbage_man:
        return "one"
    else:
        return "none"


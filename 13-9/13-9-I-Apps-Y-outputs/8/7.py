
def get_attacking_dogs(a, b, c, d, p, m, g):
    # Calculate the minute in the day when the dogs are aggressive
    aggressive_minute_postman = (p - 1) % (a + b) < a
    aggressive_minute_milkman = (m - 1) % (c + d) < c
    aggressive_minute_garbage_man = (g - 1) % (c + d) < c

    # Check if any of the dogs are aggressive
    if aggressive_minute_postman and aggressive_minute_milkman and aggressive_minute_garbage_man:
        return "both"
    elif aggressive_minute_postman xor aggressive_minute_milkman xor aggressive_minute_garbage_man:
        return "one"
    else:
        return "none"


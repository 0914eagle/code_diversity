
def divisibility_hack(b, d):
    # Initialize m to 1
    m = 1
    # Loop until m is a multiple of d
    while m % d != 0:
        # Increment m
        m += 1
    # Return yes if m is a multiple of d
    if m % d == 0:
        return "yes"
    # Otherwise, return no
    else:
        return "no"


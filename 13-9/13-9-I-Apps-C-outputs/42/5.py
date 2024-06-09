
def divisibility_hack(b, d):
    # Initialize m to 1
    m = 1
    # Loop until m exceeds b
    while m <= b:
        # Check if b^m is divisible by d
        if b**m % d == 0:
            # If it is, return "yes"
            return "yes"
        # Increment m
        m += 1
    # If no value of m works, return "no"
    return "no"


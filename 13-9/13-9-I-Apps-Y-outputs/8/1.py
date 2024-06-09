
def solve(a, b, c, d, p, m, g):
    # Calculate the time when the dogs are aggressive
    aggressive_time_dog_1 = (p + m + g) % (a + b)
    aggressive_time_dog_2 = (p + m + g) % (c + d)

    # Check if both dogs are aggressive
    if aggressive_time_dog_1 == 0 and aggressive_time_dog_2 == 0:
        return "both"

    # Check if only one dog is aggressive
    elif aggressive_time_dog_1 == 0 or aggressive_time_dog_2 == 0:
        return "one"

    # Check if no dog is aggressive
    else:
        return "none"


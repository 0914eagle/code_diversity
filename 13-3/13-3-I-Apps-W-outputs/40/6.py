
def get_max_score(numbers):
    # Calculate the greatest common divisor of all numbers
    gcd = functools.reduce(math.gcd, numbers)
    # Calculate the least common multiple of all numbers
    lcm = functools.reduce(lambda a, b: a * b // math.gcd(a, b), numbers)
    return gcd, lcm // gcd


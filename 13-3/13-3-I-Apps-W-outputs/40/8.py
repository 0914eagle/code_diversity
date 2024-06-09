
def get_maximum_score(numbers):
    # Calculate the greatest common divisor of all numbers
    gcd = numbers[0]
    for i in range(1, len(numbers)):
        gcd = gcd(numbers[i], gcd)
    
    # Calculate the least common multiple of all numbers
    lcm = 1
    for i in range(len(numbers)):
        lcm = lcm * numbers[i] // gcd
    
    return lcm, len(numbers)


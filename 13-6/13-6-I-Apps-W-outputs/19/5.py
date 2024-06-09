
def get_maximum_fruits(lemons, apples, pears):
    # Find the least common multiple of lemons, apples, and pears
    lcm = lemons * apples * pears / gcd(lemons, apples, pears)

    # Divide the fruits into the least common multiple
    lemon_count = lcm // lemons
    apple_count = lcm // apples
    pear_count = lcm // pears

    # Return the total number of fruits
    return lemon_count + apple_count + pear_count

def gcd(a, b, c):
    # Find the greatest common divisor of a, b, and c
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    lemons = int(input())
    apples = int(input())
    pears = int(input())
    print(get_maximum_fruits(lemons, apples, pears))


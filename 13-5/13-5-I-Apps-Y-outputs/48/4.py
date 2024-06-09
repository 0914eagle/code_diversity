
def get_min_x(divisors):
    # Sort the divisors in ascending order
    divisors.sort()
    # Initialize the minimum possible x as the product of the divisors
    x = 1
    for d in divisors:
        x *= d
    # Iterate through the divisors and check if they are actually divisors of x
    for d in divisors:
        if x % d != 0:
            return -1
    return x

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        divisors = [int(x) for x in input().split()]
        print(get_min_x(divisors))

if __name__ == '__main__':
    main()



def get_min_x(divisors):
    # Sort the divisors in ascending order
    divisors.sort()
    # Initialize the minimum possible x as the product of the divisors
    x = 1
    for d in divisors:
        x *= d
    # If the number of divisors is odd, we can remove the last divisor and still have a valid list of almost all divisors
    if len(divisors) % 2 == 1:
        x //= divisors[-1]
    return x

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        divisors = [int(x) for x in input().split()]
        x = get_min_x(divisors)
        print(x)

if __name__ == '__main__':
    main()


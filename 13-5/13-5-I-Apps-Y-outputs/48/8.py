
def get_min_x(divisors):
    # Sort the divisors in ascending order
    divisors.sort()
    # Initialize the minimum possible x as the product of the divisors
    x = 1
    for d in divisors:
        x *= d
    # If the product of the divisors is not a perfect square, it is impossible to find such number x
    if x % 2 == 1:
        return -1
    # Otherwise, return the square root of the product of the divisors
    return int(x ** 0.5)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        divisors = [int(x) for x in input().split()]
        print(get_min_x(divisors))

if __name__ == '__main__':
    main()


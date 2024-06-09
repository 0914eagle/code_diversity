
def get_min_x(divisors):
    # Sort the divisors in ascending order
    divisors.sort()
    # Initialize the minimum possible value of x as the smallest divisor
    x = divisors[0]
    # Iterate through the divisors and find the smallest value of x that is greater than or equal to the product of all the divisors
    for i in range(1, len(divisors)):
        x = max(x, divisors[i] // x)
    return x

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        divisors = list(map(int, input().split()))
        x = get_min_x(divisors)
        print(x)

if __name__ == '__main__':
    main()


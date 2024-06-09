
def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    divisors.sort()
    return divisors

def restore_numbers(divisors):
    x = 1
    y = 1
    for d in divisors:
        if d == 1:
            continue
        while x % d != 0:
            x *= d
        while y % d != 0:
            y *= d
    return x, y

def main():
    n = int(input())
    divisors = list(map(int, input().split()))
    x, y = restore_numbers(divisors)
    print(x, y)

if __name__ == '__main__':
    main()


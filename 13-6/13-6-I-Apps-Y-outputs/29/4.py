
def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    return sorted(divisors)

def restore_numbers(divisors):
    x = 1
    y = 1
    for d in divisors:
        if d == 1:
            continue
        while x % d != 0 or y % d != 0:
            x *= d
            y *= d
    return x, y

def main():
    n = int(input())
    divisors = sorted(list(map(int, input().split())))
    x, y = restore_numbers(divisors)
    print(x)
    print(y)

if __name__ == '__main__':
    main()



def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    return sorted(divisors)

def get_x_and_y(divisors):
    x = 1
    y = 1
    for d in divisors:
        x *= d
        y *= d
    return x, y

def main():
    n = int(input())
    divisors = sorted(list(set(map(int, input().split()))))
    x, y = get_x_and_y(divisors)
    print(x, y)

if __name__ == '__main__':
    main()


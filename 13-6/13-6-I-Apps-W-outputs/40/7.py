
def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    divisors.sort()
    return divisors

def sum_of_divisors(n):
    divisors = get_divisors(n)
    return sum(d * (d + 1) // 2 for d in divisors)

def solve(n):
    return sum(sum_of_divisors(k) for k in range(1, n + 1))

if __name__ == '__main__':
    n = int(input())
    print(solve(n))


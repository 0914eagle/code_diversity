
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
    return sum(get_divisors(n))

def solve(n):
    return sum(k * sum_of_divisors(k) for k in range(1, n + 1))

if __name__ == '__main__':
    n = int(input())
    print(solve(n))



def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    divisors.sort()
    return divisors

def solve(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * len(get_divisors(i))
    return sum

if __name__ == '__main__':
    n = int(input())
    print(solve(n))


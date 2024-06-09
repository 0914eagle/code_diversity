
def get_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def solve(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = (factorial * i) % 1000000007
    divisors = get_divisors(factorial)
    return len(divisors)

if __name__ == '__main__':
    n = int(input())
    print(solve(n))



def divisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def solve(n):
    return divisors(factorial(n))

if __name__ == '__main__':
    n = int(input())
    print(solve(n))


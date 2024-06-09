
def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    divisors.sort()
    return divisors

def get_prime_divisors(n):
    prime_divisors = []
    for i in get_divisors(n):
        if is_prime(i):
            prime_divisors.append(i)
    return prime_divisors

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_shortest_paths(v, u):
    shortest_paths = []
    for divisor in get_divisors(v):
        if divisor >= u:
            break
        for prime_divisor in get_prime_divisors(divisor):
            if prime_divisor >= u:
                break
            shortest_paths.append([divisor, prime_divisor])
    return shortest_paths

def count_shortest_paths(v, u):
    count = 0
    for shortest_path in get_shortest_paths(v, u):
        count += 1
    return count

if __name__ == '__main__':
    D = int(input())
    q = int(input())
    for _ in range(q):
        v, u = map(int, input().split())
        print(count_shortest_paths(v, u) % 998244353)


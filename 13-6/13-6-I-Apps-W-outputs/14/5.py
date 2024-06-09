
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
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and is_prime(i):
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
    divisors = get_divisors(v)
    prime_divisors = get_prime_divisors(v)
    paths = []
    for d in divisors:
        if d >= u:
            break
        if d in prime_divisors:
            paths.append([d])
        else:
            for pd in prime_divisors:
                if d * pd >= u:
                    break
                paths.append([d, pd])
    return paths

def main():
    d = int(input())
    q = int(input())
    for i in range(q):
        v, u = map(int, input().split())
        paths = get_shortest_paths(v, u)
        print(len(paths) % 998244353)

if __name__ == '__main__':
    main()


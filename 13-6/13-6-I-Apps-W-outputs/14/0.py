
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
    shortest_paths = []
    queue = [(v, [])]
    while queue:
        (node, path) = queue.pop(0)
        if node == u:
            shortest_paths.append(path)
        for neighbor in get_divisors(node):
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
    return shortest_paths

def get_number_of_shortest_paths(v, u):
    return len(get_shortest_paths(v, u))

def main():
    D = int(input())
    q = int(input())
    for _ in range(q):
        v, u = map(int, input().split())
        print(get_number_of_shortest_paths(v, u) % 998244353)

if __name__ == '__main__':
    main()


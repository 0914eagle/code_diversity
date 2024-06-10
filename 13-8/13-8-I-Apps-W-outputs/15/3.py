
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_relatively_prime(n, m):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and m % i == 0:
            return False
    return True

def construct_relatively_prime_graph(n, m):
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if is_relatively_prime(i+1, j+1) and len(edges) < m:
                edges.append((i+1, j+1))
    return edges

def main():
    n, m = map(int, input().split())
    if n * (n-1) // 2 < m:
        print("Impossible")
    else:
        print("Possible")
        for edge in construct_relatively_prime_graph(n, m):
            print(edge[0], edge[1])

if __name__ == '__main__':
    main()


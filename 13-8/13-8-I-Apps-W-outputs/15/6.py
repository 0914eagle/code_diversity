
def is_relatively_prime(n, m):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and m % i == 0:
            return False
    return True

def construct_relatively_prime_graph(n, m):
    if m > n * (n - 1) // 2:
        return "Impossible"
    
    edges = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if is_relatively_prime(i, j) and (i, j) not in edges:
                edges.append((i, j))
                m -= 1
                if m == 0:
                    break
        if m == 0:
            break
    
    return "Possible\n" + "\n".join(f"{i} {j}" for i, j in edges)

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(construct_relatively_prime_graph(n, m))


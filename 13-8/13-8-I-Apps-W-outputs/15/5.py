
def is_relatively_prime(v, u):
    return gcd(v, u) == 1

def construct_relatively_prime_graph(n, m):
    edges = []
    for i in range(m):
        v, u = map(int, input().split())
        if not is_relatively_prime(v, u):
            return "Impossible"
        edges.append((v, u))
    return edges

def main():
    n, m = map(int, input().split())
    edges = construct_relatively_prime_graph(n, m)
    if edges == "Impossible":
        print(edges)
    else:
        print("Possible")
        for edge in edges:
            print(edge[0], edge[1])

if __name__ == '__main__':
    main()



def get_boring_pairs(planets, paths):
    boring_pairs = 0
    for i in range(len(planets)):
        for j in range(i+1, len(planets)):
            if planets[i] != planets[j] and paths[i][j] == 0:
                boring_pairs += 1
    return boring_pairs

def get_boring_pairs_after_destruction(planets, paths, destruction_order):
    boring_pairs = get_boring_pairs(planets, paths)
    for path in destruction_order:
        boring_pairs -= 1
        if paths[path][path+1] == 0:
            boring_pairs -= 1
    return boring_pairs

if __name__ == '__main__':
    N = int(input())
    planets = list(range(1, N+1))
    paths = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N-1):
        A, B, Z = map(int, input().split())
        paths[A][B] = Z
        paths[B][A] = Z
    destruction_order = list(map(int, input().split()))
    for i in range(N):
        print(get_boring_pairs_after_destruction(planets, paths, destruction_order[:i+1]))


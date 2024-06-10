
def get_boring_pairs(planets, paths, n):
    boring_pairs = 0
    for i in range(n):
        path = paths[i]
        for j in range(i+1, n):
            if path[0] == paths[j][0] or path[1] == paths[j][1]:
                boring_pairs += 1
    return boring_pairs

def get_boring_pairs_after_destruction(planets, paths, n, permutation):
    boring_pairs = 0
    for i in range(n):
        path = paths[permutation[i]-1]
        for j in range(i+1, n):
            if path[0] == paths[permutation[j]-1][0] or path[1] == paths[permutation[j]-1][1]:
                boring_pairs += 1
    return boring_pairs

if __name__ == '__main__':
    num_planets = int(input())
    planets = []
    paths = []
    for i in range(num_planets-1):
        planets.append(list(map(int, input().split())))
        paths.append(list(map(int, input().split())))
    permutation = list(map(int, input().split()))
    print(get_boring_pairs(planets, paths, num_planets-1))
    for i in range(1, num_planets):
        print(get_boring_pairs_after_destruction(planets, paths, num_planets-1, permutation[:i]))



import sys
import itertools

def get_boring_pairs(planets, paths):
    boring_pairs = set()
    for i in range(len(planets)):
        for j in range(i + 1, len(planets)):
            if (planets[i], planets[j]) in boring_pairs:
                continue
            xor = 0
            for path in paths:
                if path[0] == planets[i] and path[1] == planets[j]:
                    xor ^= path[2]
                elif path[0] == planets[j] and path[1] == planets[i]:
                    xor ^= path[2]
            if xor == 0:
                boring_pairs.add((planets[i], planets[j]))
    return boring_pairs

def get_boring_pairs_after_destroying_paths(planets, paths, destroyed_paths):
    destroyed_paths_set = set(destroyed_paths)
    boring_pairs = set()
    for i in range(len(planets)):
        for j in range(i + 1, len(planets)):
            if (planets[i], planets[j]) in boring_pairs:
                continue
            xor = 0
            for path in paths:
                if path[0] == planets[i] and path[1] == planets[j] and path not in destroyed_paths_set:
                    xor ^= path[2]
                elif path[0] == planets[j] and path[1] == planets[i] and path not in destroyed_paths_set:
                    xor ^= path[2]
            if xor == 0:
                boring_pairs.add((planets[i], planets[j]))
    return boring_pairs

def main():
    num_planets = int(input())
    planets = list(range(1, num_planets + 1))
    paths = []
    for _ in range(num_planets - 1):
        path = list(map(int, input().split()))
        paths.append(path)
    permutation = list(map(int, input().split()))
    boring_pairs = get_boring_pairs(planets, paths)
    for i in range(1, num_planets):
        destroyed_paths = permutation[:i]
        boring_pairs_after_destroying = get_boring_pairs_after_destroying_paths(planets, paths, destroyed_paths)
        print(len(boring_pairs_after_destroying))

if __name__ == '__main__':
    main()



import math

def find_distances(toys, trees):
    distances = []
    for toy in toys:
        min_distance = math.inf
        for tree in trees:
            distance = math.sqrt((toy[0] - tree[0])**2 + (toy[1] - tree[1])**2)
            min_distance = min(min_distance, distance)
        distances.append(min_distance)
    return distances

def find_leash_length(distances, trees):
    leash_length = 0
    for distance in distances:
        leash_length += distance
    return leash_length

def main():
    n, m = map(int, input().split())
    toys = []
    for i in range(n):
        x, y = map(int, input().split())
        toys.append((x, y))
    trees = []
    for i in range(m):
        x, y = map(int, input().split())
        trees.append((x, y))
    distances = find_distances(toys, trees)
    leash_length = find_leash_length(distances, trees)
    print(round(leash_length, 2))

if __name__ == '__main__':
    main()


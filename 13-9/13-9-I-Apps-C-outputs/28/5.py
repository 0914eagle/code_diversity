
import itertools

def get_pairs(universities, n):
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            pairs.append((universities[i], universities[j]))
    return pairs

def get_distances(pairs, n):
    distances = []
    for i in range(n):
        for j in range(i+1, n):
            distances.append(abs(pairs[i][0] - pairs[j][1]) + abs(pairs[i][1] - pairs[j][0]))
    return distances

def get_maximum_distance(distances):
    return max(distances)

def main():
    n, k = map(int, input().split())
    universities = list(map(int, input().split()))
    pairs = get_pairs(universities, k)
    distances = get_distances(pairs, k)
    maximum_distance = get_maximum_distance(distances)
    print(maximum_distance)

if __name__ == '__main__':
    main()


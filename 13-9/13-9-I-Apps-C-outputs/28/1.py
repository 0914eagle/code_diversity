
def read_input():
    n, k = map(int, input().split())
    universities = set(map(int, input().split()))
    roads = []
    for _ in range(n - 1):
        x, y = map(int, input().split())
        roads.append((x, y))
    return n, k, universities, roads

def pairwise_distance(pairs):
    total_distance = 0
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            total_distance += distance(pairs[i], pairs[j])
    return total_distance

def distance(pair1, pair2):
    town1, town2 = pair1
    town3, town4 = pair2
    if town1 == town3:
        return distance(pair2, pair1)
    for road in roads:
        if (road[0] == town1 and road[1] == town3) or (road[0] == town3 and road[1] == town1):
            return 1
    for road in roads:
        if (road[0] == town2 and road[1] == town4) or (road[0] == town4 and road[1] == town2):
            return 1
    return 0

def find_maximum_pairwise_distance(universities, k):
    pairs = []
    for i in range(k):
        pairs.append((universities.pop(), universities.pop()))
    return pairwise_distance(pairs)

def main():
    n, k, universities, roads = read_input()
    print(find_maximum_pairwise_distance(universities, k))

if __name__ == '__main__':
    main()


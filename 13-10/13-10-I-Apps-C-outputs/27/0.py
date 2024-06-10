
def get_input():
    n, k = map(int, input().split())
    universities = list(map(int, input().split()))
    roads = []
    for i in range(n - 1):
        x, y = map(int, input().split())
        roads.append((x, y))
    return n, k, universities, roads

def get_pairs(universities, k):
    pairs = []
    for i in range(k):
        pairs.append((universities[2*i], universities[2*i+1]))
    return pairs

def get_distance(pairs, roads):
    distance = 0
    for pair in pairs:
        for road in roads:
            if pair[0] in road and pair[1] in road:
                distance += 1
                break
    return distance

def main():
    n, k, universities, roads = get_input()
    pairs = get_pairs(universities, k)
    distance = get_distance(pairs, roads)
    print(distance)

if __name__ == '__main__':
    main()


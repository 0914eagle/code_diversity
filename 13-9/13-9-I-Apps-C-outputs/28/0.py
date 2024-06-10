
def get_universities_pairs(universities, n):
    pairs = []
    for i in range(n):
        pair = [universities[i], universities[n+i]]
        pairs.append(pair)
    return pairs

def get_pairs_distances(pairs, roads):
    distances = []
    for pair in pairs:
        distance = 0
        for i in range(len(pair)-1):
            distance += get_distance(pair[i], pair[i+1], roads)
        distances.append(distance)
    return distances

def get_distance(town1, town2, roads):
    for road in roads:
        if town1 in road and town2 in road:
            return 1
    return 0

def get_maximum_sum(distances):
    return sum(distances)

def main():
    universities = [1, 5, 6, 2, 3, 7, 4]
    n = 7
    k = 2
    roads = [[1, 3], [3, 2], [4, 5], [3, 7], [4, 3], [4, 6], [2, 1], [2, 8]]
    pairs = get_universities_pairs(universities, n)
    distances = get_pairs_distances(pairs, roads)
    maximum_sum = get_maximum_sum(distances)
    print(maximum_sum)

if __name__ == '__main__':
    main()


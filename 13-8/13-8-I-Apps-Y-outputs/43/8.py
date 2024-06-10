
def get_elevations(n):
    return list(map(int, input().split()))

def get_roads(m):
    roads = []
    for _ in range(m):
        roads.append(list(map(int, input().split())))
    return roads

def get_good_observatories(n, roads):
    elevations = get_elevations(n)
    good_observatories = []
    for i in range(n):
        max_elevation = elevations[i]
        for road in roads:
            if road[0] == i:
                max_elevation = max(max_elevation, elevations[road[1]])
        if max_elevation == elevations[i]:
            good_observatories.append(i)
    return good_observatories

def main():
    n, m = map(int, input().split())
    roads = get_roads(m)
    good_observatories = get_good_observatories(n, roads)
    print(len(good_observatories))

if __name__ == '__main__':
    main()


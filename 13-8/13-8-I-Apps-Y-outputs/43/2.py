
def get_elevations(n):
    return list(map(int, input().split()))

def get_roads(m):
    roads = []
    for _ in range(m):
        roads.append(list(map(int, input().split())))
    return roads

def is_good_observatory(observatory, elevations, roads):
    for road in roads:
        if road[0] == observatory:
            if elevations[road[1]] > elevations[observatory]:
                return False
    return True

def count_good_observatories(n, m, elevations, roads):
    good_observatories = 0
    for observatory in range(n):
        if is_good_observatory(observatory, elevations, roads):
            good_observatories += 1
    return good_observatories

def main():
    n, m = map(int, input().split())
    elevations = get_elevations(n)
    roads = get_roads(m)
    print(count_good_observatories(n, m, elevations, roads))

if __name__ == '__main__':
    main()


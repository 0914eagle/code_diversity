
def read_input():
    N = int(input())
    cities = []
    for i in range(N):
        y, d, r = map(int, input().split())
        cities.append((y, d, r))
    return N, cities

def get_shortest_time(cities):
    times = [0] * len(cities)
    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            y1, d1, r1 = cities[i]
            y2, d2, r2 = cities[j]
            if abs(y1 - y2) >= d1:
                times[j] = max(times[j], times[i] + abs(y1 - y2) + r1)
    return times

def main():
    N, cities = read_input()
    times = get_shortest_time(cities)
    for time in times[1:]:
        print(time if time != 0 else -1)

if __name__ == '__main__':
    main()


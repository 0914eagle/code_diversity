
def read_input():
    N = int(input())
    cities = []
    for i in range(N):
        y, d, r = map(int, input().split())
        cities.append((y, d, r))
    return N, cities

def solve(N, cities):
    times = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue
            y1, d1, r1 = cities[i - 1]
            y2, d2, r2 = cities[j - 1]
            if abs(y1 - y2) >= d1:
                times[j] = max(times[j], times[i] + abs(y1 - y2) + r1)
    return times[1:]

def main():
    N, cities = read_input()
    times = solve(N, cities)
    for time in times:
        print(time if time != float('inf') else -1)

if __name__ == '__main__':
    main()


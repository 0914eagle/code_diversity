
n, k, s, t = map(int, input().split())
cars = []
for _ in range(n):
    c, v = map(int, input().split())
    cars.append((c, v))

gas_stations = list(map(int, input().split()))
gas_stations.sort()

def time_to_reach_destination(car, gas_stations, s, t):
    for i in range(len(gas_stations)):
        dist_to_next_station = gas_stations[i] - (gas_stations[i-1] if i > 0 else 0)
        time_to_next_station = dist_to_next_station * 2 if car[1] >= dist_to_next_station else dist_to_next_station
        t -= time_to_next_station
        if t < 0:
            return False
    time_to_cinema = s - gas_stations[-1]
    time_to_cinema = time_to_cinema * 2 if car[1] >= time_to_cinema else time_to_cinema
    t -= time_to_cinema
    return t >= 0

min_price = float('inf')
for car in cars:
    if time_to_reach_destination(car, gas_stations, s, t):
        min_price = min(min_price, car[0])

if min_price == float('inf'):
    print(-1)
else:
    print(min_price)

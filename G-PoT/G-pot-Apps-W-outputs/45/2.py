
n, k, s, t = map(int, input().split())
cars = []
for _ in range(n):
    c, v = map(int, input().split())
    cars.append((c, v))
gas_stations = list(map(int, input().split()))

def time_to_reach_destination(car, gas_stations, s, t):
    min_time = float('inf')
    for i in range(len(gas_stations) + 1):
        dist_to_gas_station = gas_stations[i] if i < len(gas_stations) else s
        dist_to_destination = s - dist_to_gas_station
        time_to_gas_station = min(dist_to_gas_station, car[1]) if car[1] >= dist_to_gas_station else float('inf')
        time_to_destination = (dist_to_destination * 2) if time_to_gas_station >= dist_to_gas_station else (dist_to_destination + (dist_to_gas_station - time_to_gas_station) * 2)
        total_time = time_to_gas_station + time_to_destination
        min_time = min(min_time, total_time)
    return min_time

min_price = float('inf')
for car in cars:
    time_taken = time_to_reach_destination(car, gas_stations, s, t)
    if time_taken <= t:
        min_price = min(min_price, car[0])

if min_price == float('inf'):
    print(-1)
else:
    print(min_price)

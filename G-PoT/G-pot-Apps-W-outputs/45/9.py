
n, k, s, t = map(int, input().split())
cars = []
for _ in range(n):
    c, v = map(int, input().split())
    cars.append((c, v))
gas_stations = list(map(int, input().split()))

def time_to_reach_destination(speed_mode, distance, fuel_consumed):
    if speed_mode == 'normal':
        time = distance * 2
    else:
        time = distance
    return time, fuel_consumed

min_price = float('inf')
for c, v in cars:
    current_price = c
    current_fuel = v
    current_position = 0
    for i in range(k+1):
        if i < k:
            distance_to_next_station = gas_stations[i] - current_position
        else:
            distance_to_next_station = s - current_position
        if current_fuel < distance_to_next_station:
            time_normal, fuel_normal = time_to_reach_destination('normal', distance_to_next_station, current_fuel)
            time_accelerated, fuel_accelerated = time_to_reach_destination('accelerated', distance_to_next_station, current_fuel)
            if time_normal <= t or time_accelerated <= t:
                current_price = min(current_price, c)
        else:
            current_fuel -= distance_to_next_station
        current_position = gas_stations[i] if i < k else s
    min_price = min(min_price, current_price)

if min_price == float('inf'):
    print(-1)
else:
    print(min_price)

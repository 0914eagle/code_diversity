
n, k, s, t = map(int, input().split())
cars = []
for _ in range(n):
    c, v = map(int, input().split())
    cars.append((c, v))
gas_stations = list(map(int, input().split()))

def time_to_reach_destination(speed_mode, distance, fuel_consumed):
    if speed_mode == 'normal':
        return distance * 2 + fuel_consumed
    else:
        return distance + fuel_consumed * 2

def can_reach_destination(car, gas_stations, s, t):
    min_time = float('inf')
    for i in range(len(gas_stations)):
        for j in range(i+1, len(gas_stations)+1):
            distance_to_gas_station = gas_stations[i] if i == 0 else gas_stations[i] - gas_stations[i-1]
            distance_to_destination = s - gas_stations[j-1] if j == len(gas_stations) else gas_stations[j] - gas_stations[j-1]
            total_distance = distance_to_gas_station + distance_to_destination
            fuel_needed = total_distance
            if car[1] >= fuel_needed:
                time = time_to_reach_destination('normal', total_distance, fuel_needed)
                min_time = min(min_time, time)
                if min_time <= t:
                    return True
            fuel_needed = total_distance * 2
            if car[1] >= fuel_needed:
                time = time_to_reach_destination('accelerated', total_distance, fuel_needed)
                min_time = min(min_time, time)
                if min_time <= t:
                    return True
    return False

min_price = float('inf')
for car in cars:
    if can_reach_destination(car, gas_stations, s, t):
        min_price = min(min_price, car[0])

if min_price == float('inf'):
    print(-1)
else:
    print(min_price)

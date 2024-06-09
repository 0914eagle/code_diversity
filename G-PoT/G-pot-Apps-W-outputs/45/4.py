
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
        return distance + fuel_consumed

def can_reach_destination(car, gas_stations, s, t):
    for i in range(len(gas_stations) + 1):
        if i == 0:
            distance_to_gas_station = gas_stations[i]
        elif i == len(gas_stations):
            distance_to_gas_station = s - gas_stations[i-1]
        else:
            distance_to_gas_station = gas_stations[i] - gas_stations[i-1]
        
        for speed_mode in ['normal', 'accelerated']:
            time_taken = time_to_reach_destination(speed_mode, distance_to_gas_station, min(car[1], distance_to_gas_station))
            if time_taken <= t:
                t -= time_taken
                t += max(0, distance_to_gas_station - car[1])
                break
        else:
            return False
    return True

min_price = float('inf')
for car in cars:
    if can_reach_destination(car, gas_stations, s, t):
        min_price = min(min_price, car[0])

if min_price == float('inf'):
    print(-1)
else:
    print(min_price)

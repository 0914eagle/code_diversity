
n, k, s, t = map(int, input().split())
cars = []
for _ in range(n):
    c, v = map(int, input().split())
    cars.append((c, v))
gas_stations = list(map(int, input().split()))

def time_to_reach_destination(speed_mode, distance, fuel_consumed):
    if speed_mode == 'normal':
        return distance * 2, fuel_consumed
    else:
        return distance, fuel_consumed * 2

def can_reach_destination(car, gas_stations, s, t):
    for i in range(len(gas_stations)):
        if i == 0:
            time, fuel = time_to_reach_destination('normal', gas_stations[i], gas_stations[i])
        else:
            time, fuel = time_to_reach_destination('normal', gas_stations[i] - gas_stations[i-1], gas_stations[i] - gas_stations[i-1])
        if time > t or fuel > car[1]:
            return False
    time, fuel = time_to_reach_destination('normal', s - gas_stations[-1], s - gas_stations[-1])
    if time > t or fuel > car[1]:
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

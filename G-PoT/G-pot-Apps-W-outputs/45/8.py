
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

def min_rent_price(n, k, s, t, cars, gas_stations):
    min_price = float('inf')
    for c, v in cars:
        time_taken = 0
        fuel_consumed = 0
        for i in range(len(gas_stations)):
            distance = gas_stations[i] - fuel_consumed
            if distance > v:
                time_taken = float('inf')
                break
            time_taken += time_to_reach_destination('normal', distance, fuel_consumed)
            fuel_consumed = gas_stations[i]
        if time_taken == float('inf'):
            continue
        distance = s - fuel_consumed
        if distance > v:
            time_taken = float('inf')
        else:
            time_taken += time_to_reach_destination('normal', distance, fuel_consumed)
        if time_taken <= t:
            min_price = min(min_price, c)
    return min_price if min_price != float('inf') else -1

print(min_rent_price(n, k, s, t, cars, gas_stations))

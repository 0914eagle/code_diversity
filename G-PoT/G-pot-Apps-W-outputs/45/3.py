
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

min_rent_price = float('inf')
for c, v in cars:
    time_taken = 0
    for i in range(k+1):
        if i == 0:
            distance = gas_stations[i]
        elif i == k:
            distance = s - gas_stations[i-1]
        else:
            distance = gas_stations[i] - gas_stations[i-1]
        
        fuel_consumed = distance
        if fuel_consumed <= v:
            time_taken += time_to_reach_destination('normal', distance, fuel_consumed)
        else:
            time_taken += time_to_reach_destination('accelerated', distance, fuel_consumed)
        
        if time_taken > t:
            break
    
    if time_taken <= t:
        min_rent_price = min(min_rent_price, c)

if min_rent_price == float('inf'):
    print(-1)
else:
    print(min_rent_price)

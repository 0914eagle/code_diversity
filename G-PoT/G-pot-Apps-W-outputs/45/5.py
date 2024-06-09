
n, k, s, t = map(int, input().split())
cars = []
for _ in range(n):
    c, v = map(int, input().split())
    cars.append((c, v))
gas_stations = list(map(int, input().split()))

def time_to_reach_destination(car, distance, fuel_needed):
    normal_time = distance * 2
    accel_time = distance
    fuel_consumed = min(fuel_needed, car[1])
    if fuel_consumed * 2 >= distance:
        return min(normal_time, accel_time)
    else:
        return float('inf')

min_price = float('inf')
for car in cars:
    total_time = 0
    for i in range(k+1):
        if i == 0:
            distance = gas_stations[i]
        elif i == k:
            distance = s - gas_stations[i-1]
        else:
            distance = gas_stations[i] - gas_stations[i-1]
        
        fuel_needed = distance
        time_taken = time_to_reach_destination(car, distance, fuel_needed)
        total_time += time_taken
        
        if total_time > t:
            break
    
    if total_time <= t:
        min_price = min(min_price, car[0])

if min_price == float('inf'):
    print(-1)
else:
    print(min_price)

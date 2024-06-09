
def get_trip_cost(trip_time):
    if trip_time <= 90:
        return 20
    elif trip_time <= 1440:
        return 50
    else:
        return 120

def get_total_cost(trip_times):
    total_cost = 0
    for trip_time in trip_times:
        total_cost += get_trip_cost(trip_time)
    return total_cost

def get_charged_amount(trip_times):
    total_cost = get_total_cost(trip_times)
    return total_cost - total_cost % 20

if __name__ == '__main__':
    num_trips = int(input())
    trip_times = []
    for _ in range(num_trips):
        trip_times.append(int(input()))
    print(get_charged_amount(trip_times))


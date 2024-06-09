
def get_fare(trip_time):
    if trip_time <= 1:
        return 20
    elif trip_time <= 90:
        return 50
    else:
        return 120

def get_charged_fare(trip_time, previous_trips):
    total_fare = 0
    for trip in previous_trips:
        total_fare += get_fare(trip)
    total_fare += get_fare(trip_time)
    return total_fare

def get_optimal_fare(trip_times):
    previous_trips = []
    optimal_fare = 0
    for trip_time in trip_times:
        charged_fare = get_charged_fare(trip_time, previous_trips)
        if charged_fare < optimal_fare:
            optimal_fare = charged_fare
        previous_trips.append(trip_time)
    return optimal_fare

if __name__ == '__main__':
    n = int(input())
    trip_times = []
    for i in range(n):
        trip_times.append(int(input()))
    print(get_optimal_fare(trip_times))


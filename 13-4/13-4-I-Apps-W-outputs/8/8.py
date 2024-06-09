
def get_fare(trip_time):
    if trip_time <= 90:
        return 20
    elif trip_time <= 1440:
        return 50
    else:
        return 120

def get_charges(trip_times):
    total_fare = 0
    for i in range(len(trip_times)):
        trip_time = trip_times[i]
        fare = get_fare(trip_time)
        total_fare += fare
        if i > 0:
            prev_trip_time = trip_times[i-1]
            prev_fare = get_fare(prev_trip_time)
            total_fare -= prev_fare
    return total_fare

if __name__ == '__main__':
    n = int(input())
    trip_times = []
    for i in range(n):
        trip_time = int(input())
        trip_times.append(trip_time)
    charges = get_charges(trip_times)
    print(charges)


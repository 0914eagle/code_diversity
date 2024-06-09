
def get_fare(trip_time):
    
    if trip_time <= 1440:
        return 20
    elif trip_time <= 2880:
        return 50
    else:
        return 120

def get_charged_fare(trip_time, previous_trips):
    
    total_fare = 0
    for previous_trip in previous_trips:
        total_fare += get_fare(previous_trip)
    total_fare += get_fare(trip_time)
    return total_fare

def get_charged_fares(trip_times):
    
    previous_trips = []
    charged_fares = []
    for trip_time in trip_times:
        charged_fare = get_charged_fare(trip_time, previous_trips)
        charged_fares.append(charged_fare)
        previous_trips.append(trip_time)
    return charged_fares

if __name__ == '__main__':
    trip_times = [int(input()) for _ in range(int(input()))]
    charged_fares = get_charged_fares(trip_times)
    for charged_fare in charged_fares:
        print(charged_fare)


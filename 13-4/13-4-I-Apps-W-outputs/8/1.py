
def get_fare(time):
    if time <= 90:
        return 20
    elif time <= 1440:
        return 50
    else:
        return 120

def get_total_fare(trips):
    total_fare = 0
    for trip in trips:
        total_fare += get_fare(trip)
    return total_fare

def get_charged_fare(trips):
    total_fare = get_total_fare(trips)
    charged_fare = total_fare
    for i in range(len(trips) - 1):
        current_trip = trips[i]
        next_trip = trips[i + 1]
        if next_trip - current_trip <= 90:
            charged_fare -= get_fare(next_trip - current_trip)
    return charged_fare

if __name__ == '__main__':
    n = int(input())
    trips = []
    for i in range(n):
        trips.append(int(input()))
    print(get_charged_fare(trips))


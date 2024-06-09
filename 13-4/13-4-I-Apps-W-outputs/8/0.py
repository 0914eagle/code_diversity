
def get_trip_cost(trip_time, current_time):
    
    if trip_time == 0:
        return 0
    elif trip_time <= 90:
        return 20
    elif trip_time <= 1440:
        return 50
    else:
        return 120

def get_total_cost(trip_times, current_time):
    
    total_cost = 0
    for trip_time in trip_times:
        total_cost += get_trip_cost(trip_time, current_time)
    return total_cost

def get_charged_amount(trip_times, current_time):
    
    total_cost = get_total_cost(trip_times, current_time)
    charged_amount = total_cost
    for i in range(len(trip_times)):
        trip_time = trip_times[i]
        if trip_time > current_time:
            charged_amount -= get_trip_cost(trip_time - current_time, current_time)
            break
        else:
            charged_amount -= get_trip_cost(trip_time, current_time)
            current_time += trip_time
    return charged_amount

def main():
    trip_times = [int(x) for x in input().split()]
    current_time = 0
    for trip_time in trip_times:
        charged_amount = get_charged_amount(trip_times, current_time)
        print(charged_amount)
        current_time += trip_time

if __name__ == '__main__':
    main()



def get_flight_times(p, q, r):
    return [p, q, r]

def get_min_flight_time(flight_times):
    return min(flight_times)

if __name__ == '__main__':
    p, q, r = map(int, input().split())
    flight_times = get_flight_times(p, q, r)
    min_flight_time = get_min_flight_time(flight_times)
    print(min_flight_time)


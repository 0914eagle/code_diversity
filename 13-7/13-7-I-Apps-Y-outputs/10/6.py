
def get_flight_times():
    return list(map(int, input().split()))

def get_min_flight_time(flight_times):
    P, Q, R = flight_times
    return min(P + Q, Q + R, R + P)

if __name__ == '__main__':
    flight_times = get_flight_times()
    print(get_min_flight_time(flight_times))


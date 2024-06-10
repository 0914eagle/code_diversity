
def get_flight_times(p, q, r):
    return p, q, r

def get_min_flight_time(p, q, r):
    flight_times = [p + q, q + r, r + p]
    return min(flight_times)

if __name__ == '__main__':
    p, q, r = map(int, input().split())
    print(get_min_flight_time(p, q, r))


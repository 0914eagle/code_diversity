
def get_flight_times(p, q, r):
    return p, q, r

def get_min_flight_time(p, q, r):
    flights = [(p, "A", "B"), (q, "B", "C"), (r, "C", "A")]
    min_time = float("inf")
    for flight in flights:
        time = flight[0]
        start = flight[1]
        end = flight[2]
        min_time = min(min_time, time)
    return min_time

def main():
    p, q, r = map(int, input().split())
    print(get_min_flight_time(p, q, r))

if __name__ == '__main__':
    main()


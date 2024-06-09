
def verify_measurements(capacity, stations):
    total = 0
    for station in stations:
        leaving, entering, waiting = station
        total += entering - leaving
        if waiting > 0 and total > capacity:
            return "impossible"
    if total != 0:
        return "impossible"
    return "possible"



def is_input_consistent(capacity, stations):
    total = 0
    for station in stations:
        leaving, entering, waiting = station
        total += entering - leaving
        if total < 0 or waiting > 0:
            return "impossible"
    return "possible" if total == 0 else "impossible"


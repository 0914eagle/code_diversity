
def is_input_consistent(capacity, measurements):
    total = 0
    for measurement in measurements:
        leaving, entering, waiting = measurement
        total += entering - leaving
        if total < 0 or waiting > 0:
            return "impossible"
    return "possible"


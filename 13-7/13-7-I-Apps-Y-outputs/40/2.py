
def is_consistent(capacity, measurements):
    total = 0
    for measurement in measurements:
        leaving, entering, staying = measurement
        total += entering - leaving
        if total < 0 or staying > 0 and total == capacity:
            return "impossible"
    return "possible"


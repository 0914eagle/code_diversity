
def verify_measurements(capacity, measurements):
    total = 0
    for measurement in measurements:
        total += measurement[0] - measurement[1]
        if total < 0 or total > capacity:
            return "impossible"
    return "possible"


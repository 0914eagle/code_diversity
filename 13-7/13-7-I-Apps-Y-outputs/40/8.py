
def is_consistent(capacity, measurements):
    total = 0
    for measurement in measurements:
        leave, enter, stay = measurement
        total += enter - leave
        if total > capacity or total < 0:
            return "impossible"
    return "possible"


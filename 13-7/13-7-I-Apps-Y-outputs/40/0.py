
def is_consistent(capacity, measurements):
    curr_capacity = 0
    for left, entered, stayed in measurements:
        curr_capacity += entered - left
        if curr_capacity > capacity or stayed > 0:
            return "impossible"
    return "possible"


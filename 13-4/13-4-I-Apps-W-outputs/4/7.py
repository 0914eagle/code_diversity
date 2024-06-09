
def get_pyramids_count(n):
    pyramids_count = 0
    while n > 0:
        pyramids_count += 1
        n -= (2 * pyramids_count) + 1
    return pyramids_count


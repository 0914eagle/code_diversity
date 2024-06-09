
def get_pyramids_count(n):
    count = 0
    while n > 0:
        count += 1
        n -= count
    return count


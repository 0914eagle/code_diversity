
def get_pyramids_constructed(n):
    pyramids_constructed = 0
    while n >= 1:
        pyramids_constructed += 1
        n -= 1
    return pyramids_constructed


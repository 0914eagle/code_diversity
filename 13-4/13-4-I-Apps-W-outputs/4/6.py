
def get_pyramids_constructed(n):
    pyramids_constructed = 0
    while n > 0:
        if n == 1:
            pyramids_constructed += 1
            break
        elif n == 2:
            pyramids_constructed += 2
            break
        else:
            pyramids_constructed += 1
            n -= 3
    return pyramids_constructed



def num_ways_to_show_fingers(n, fingers):
    total_fingers = sum(fingers)
    ways = 0
    for i in range(1, 6):
        if i != total_fingers:
            ways += 1
    return ways


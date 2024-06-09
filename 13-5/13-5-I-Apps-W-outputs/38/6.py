
def count_ways_to_clean(n, fingers):
    total_fingers = sum(fingers)
    ways_to_clean = 0
    for i in range(1, 6):
        if i != total_fingers:
            ways_to_clean += 1
    return ways_to_clean


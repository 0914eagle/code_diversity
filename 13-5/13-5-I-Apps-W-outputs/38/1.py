
def count_ways_to_not_clean(n, friends_fingers):
    total_fingers = sum(friends_fingers)
    ways_to_not_clean = 0
    for i in range(1, 6):
        if i != total_fingers:
            ways_to_not_clean += 1
    return ways_to_not_clean


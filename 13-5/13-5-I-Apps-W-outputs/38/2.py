
def solve(n, fingers):
    total_fingers = sum(fingers)
    ways_to_show_fingers = 0
    for i in range(1, 6):
        if total_fingers - i not in fingers:
            ways_to_show_fingers += 1
    return ways_to_show_fingers


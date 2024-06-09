
def solve(n, fingers):
    total_fingers = sum(fingers)
    ways = 0
    for i in range(1, 6):
        if i != total_fingers:
            ways += 1
    return ways



def clockwise_distance(start, end, total_positions):
    return (end - start) % total_positions

def counterclockwise_distance(start, end, total_positions):
    return (start - end) % total_positions

def can_prepare_contest(h, m, s, t1, t2):
    clock_positions = [h, m, s]
    t1, t2 = sorted([t1, t2])

    hour_hand, minute_hand, second_hand = clock_positions
    total_positions = 12

    clockwise_dist = clockwise_distance(t1, t2, total_positions)
    counterclockwise_dist = counterclockwise_distance(t1, t2, total_positions)

    hour_diff = clockwise_distance(hour_hand, minute_hand, total_positions)
    minute_diff = clockwise_distance(minute_hand, second_hand, total_positions)
    second_diff = clockwise_distance(second_hand, hour_hand, total_positions)

    if (clockwise_dist <= hour_diff and clockwise_dist <= minute_diff and clockwise_dist <= second_diff) or \
            (counterclockwise_dist <= hour_diff and counterclockwise_dist <= minute_diff and counterclockwise_dist <= second_diff):
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    h, m, s, t1, t2 = map(int, input().split())
    print(can_prepare_contest(h, m, s, t1, t2))

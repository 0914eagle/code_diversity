
def can_prepare_contest(h, m, s, t1, t2):
    def clockwise_distance(start, end, total):
        return (end - start + total) % total

    def counterclockwise_distance(start, end, total):
        return (start - end + total) % total

    total_positions = 12

    hour_hand = h
    minute_hand = m / 5
    second_hand = s / 5

    clockwise_hour_distance = clockwise_distance(t1, t2, total_positions)
    counterclockwise_hour_distance = counterclockwise_distance(t1, t2, total_positions)

    if (clockwise_hour_distance * 5 <= hour_hand and
            clockwise_hour_distance * 5 <= minute_hand and
            clockwise_hour_distance * 5 <= second_hand) or \
            (counterclockwise_hour_distance * 5 <= hour_hand and
             counterclockwise_hour_distance * 5 <= minute_hand and
             counterclockwise_hour_distance * 5 <= second_hand):
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    h, m, s, t1, t2 = map(int, input().split())
    result = can_prepare_contest(h, m, s, t1, t2)
    print(result)

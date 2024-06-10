
def calculate_distance_clockwise(start, end):
    if start <= end:
        return end - start
    else:
        return 12 - start + end

def calculate_distance_counterclockwise(start, end):
    if start >= end:
        return start - end
    else:
        return start + 12 - end

def can_prepare_contest(h, m, s, t1, t2):
    hour_hand = h
    minute_hand = m / 5  # Normalize to clock positions
    second_hand = s / 5  # Normalize to clock positions

    clockwise_distance = calculate_distance_clockwise(t1, t2)
    counterclockwise_distance = calculate_distance_counterclockwise(t1, t2)

    if (clockwise_distance * 5 <= hour_hand or counterclockwise_distance * 5 <= hour_hand) and \
       (clockwise_distance * 5 <= minute_hand or counterclockwise_distance * 5 <= minute_hand) and \
       (clockwise_distance * 5 <= second_hand or counterclockwise_distance * 5 <= second_hand):
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    h, m, s, t1, t2 = map(int, input().split())
    result = can_prepare_contest(h, m, s, t1, t2)
    print(result)


def calculate_distance_clockwise(start, end):
    return (end - start) % 12

def calculate_distance_counterclockwise(start, end):
    return (start - end) % 12

def can_prepare_contest(h, m, s, t1, t2):
    hour_hand = h
    minute_hand = m / 5
    second_hand = s / 5

    clockwise_distance = calculate_distance_clockwise(t1, t2)
    counterclockwise_distance = calculate_distance_counterclockwise(t1, t2)

    if (clockwise_distance <= hour_hand and clockwise_distance <= minute_hand and clockwise_distance <= second_hand) or \
       (counterclockwise_distance <= hour_hand and counterclockwise_distance <= minute_hand and counterclockwise_distance <= second_hand):
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    h, m, s, t1, t2 = map(int, input().split())
    result = can_prepare_contest(h, m, s, t1, t2)
    print(result)

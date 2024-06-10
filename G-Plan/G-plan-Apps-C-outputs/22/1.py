
def calculate_clockwise_distance(start, end):
    return (end - start) % 12

def calculate_counterclockwise_distance(start, end):
    return (start - end) % 12

def can_prepare_contest(h, m, s, t1, t2):
    hour_hand = h
    minute_hand = m / 5
    second_hand = s / 5

    clockwise_distance = calculate_clockwise_distance(t1, t2)
    counterclockwise_distance = calculate_counterclockwise_distance(t1, t2)

    if (clockwise_distance <= hour_hand or clockwise_distance <= minute_hand or clockwise_distance <= second_hand) or \
       (counterclockwise_distance <= hour_hand or counterclockwise_distance <= minute_hand or counterclockwise_distance <= second_hand):
        return "NO"
    else:
        return "YES"

if __name__ == "__main__":
    h, m, s, t1, t2 = map(int, input().split())
    result = can_prepare_contest(h, m, s, t1, t2)
    print(result)

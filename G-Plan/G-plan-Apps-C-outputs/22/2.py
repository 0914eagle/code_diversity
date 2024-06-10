
def can_prepare_contest(h, m, s, t1, t2):
    def clockwise_distance(start, end, total):
        return (end - start) % total

    def counterclockwise_distance(start, end, total):
        return (start - end) % total

    clock_total = 12
    hour_hand = h % 12
    minute_hand = m / 5
    second_hand = s / 5

    clockwise_hour = clockwise_distance(t1, t2, clock_total)
    counterclockwise_hour = counterclockwise_distance(t1, t2, clock_total)

    if (clockwise_hour != 0 and clockwise_hour != 1 and clockwise_hour != 11) or (counterclockwise_hour != 0 and counterclockwise_hour != 1 and counterclockwise_hour != 11):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    h, m, s, t1, t2 = map(int, input().split())
    can_prepare_contest(h, m, s, t1, t2)

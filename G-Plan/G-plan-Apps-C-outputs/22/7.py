
def can_prepare_contest(h, m, s, t1, t2):
    def clockwise_distance(start, end, total_positions):
        return (end - start) % total_positions

    def counterclockwise_distance(start, end, total_positions):
        return (start - end) % total_positions

    clock_positions = [h, m, s]
    clockwise_dist = clockwise_distance(t1, t2, 12)
    counterclockwise_dist = counterclockwise_distance(t1, t2, 12)

    for pos in clock_positions:
        if clockwise_dist == clockwise_distance(t1, pos, 12) + clockwise_distance(pos, t2, 12) or \
           counterclockwise_dist == counterclockwise_distance(t1, pos, 12) + counterclockwise_distance(pos, t2, 12):
            return "NO"
    
    return "YES"

if __name__ == "__main__":
    h, m, s, t1, t2 = map(int, input().split())
    print(can_prepare_contest(h, m, s, t1, t2))

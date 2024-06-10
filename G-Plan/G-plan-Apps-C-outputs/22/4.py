
def can_prepare_contest(h, m, s, t1, t2):
    # Calculate clockwise and counterclockwise distances
    clockwise_dist = (t2 - t1) % 12
    counterclockwise_dist = (t1 - t2) % 12

    # Check if Misha can move without crossing clock hands
    if clockwise_dist == 0 or counterclockwise_dist == 0:
        return "NO"
    elif clockwise_dist in [3, 6, 9] or counterclockwise_dist in [3, 6, 9]:
        return "NO"
    else:
        return "YES"

if __name__ == "__main__":
    h, m, s, t1, t2 = map(int, input().split())
    result = can_prepare_contest(h, m, s, t1, t2)
    print(result)

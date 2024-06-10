
def get_time_difference(t_1, t_2):
    return abs(t_1 - t_2)

def get_hand_position(h, m, s):
    return (h * 60 + m) * 60 + s

def can_move_to_time(t_1, t_2, hand_positions):
    time_difference = get_time_difference(t_1, t_2)
    hand_position = get_hand_position(t_1.hour, t_1.minute, t_1.second)
    for hand in hand_positions:
        if hand_position == hand:
            return False
    return True

def main():
    h, m, s, t_1, t_2 = map(int, input().split())
    hand_positions = [get_hand_position(h, m, s), get_hand_position(t_1.hour, t_1.minute, t_1.second), get_hand_position(t_2.hour, t_2.minute, t_2.second)]
    if can_move_to_time(t_1, t_2, hand_positions):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()


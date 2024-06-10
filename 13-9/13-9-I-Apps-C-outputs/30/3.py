
def get_time_difference(t1, t2):
    return abs(t1 - t2)

def get_hands_position(h, m, s):
    return (h, m, s)

def can_move_to_target_time(hands_position, target_time):
    current_time = get_time_difference(hands_position[0], hands_position[1])
    if current_time == target_time:
        return True
    
    for i in range(1, 3):
        if get_time_difference(hands_position[i], target_time) < current_time:
            return False
    
    return True

def main():
    h, m, s, t1, t2 = map(int, input().split())
    hands_position = get_hands_position(h, m, s)
    target_time = get_time_difference(t1, t2)
    can_move = can_move_to_target_time(hands_position, target_time)
    print("YES" if can_move else "NO")

if __name__ == '__main__':
    main()


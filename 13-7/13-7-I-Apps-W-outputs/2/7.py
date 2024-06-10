
def get_status(statuses):
    allin_count = 0
    for status in statuses:
        if status == "ALLIN":
            allin_count += 1
    return allin_count

def can_show_hands(statuses, allin_count):
    can_show_hands_count = 0
    for status in statuses:
        if status == "ALLIN" or status == "FOLDED":
            can_show_hands_count += 1
    return can_show_hands_count

def main():
    n = int(input())
    statuses = input()
    allin_count = get_status(statuses)
    can_show_hands_count = can_show_hands(statuses, allin_count)
    print(can_show_hands_count)

if __name__ == '__main__':
    main()


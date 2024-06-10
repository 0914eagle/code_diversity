
def get_num_showable_hands(statuses):
    num_allin = statuses.count("A")
    num_in = statuses.count("I")
    num_folded = statuses.count("F")
    num_showable = 0
    if num_allin == len(statuses):
        num_showable = len(statuses)
    elif num_allin + num_folded == len(statuses):
        num_showable = num_allin
    elif num_allin + num_in == len(statuses):
        num_showable = num_allin + num_in
    return num_showable

def main():
    num_cows = int(input())
    statuses = input()
    num_showable_hands = get_num_showable_hands(statuses)
    print(num_showable_hands)

if __name__ == '__main__':
    main()


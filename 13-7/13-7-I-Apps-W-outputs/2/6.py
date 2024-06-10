
def get_number_of_showable_hands(statuses):
    num_showable_hands = 0
    for i, status in enumerate(statuses):
        if status == "F":
            continue
        if all(statuses[j] in ("F", "A") for j in range(len(statuses)) if j != i):
            num_showable_hands += 1
    return num_showable_hands

def main():
    num_cows = int(input())
    statuses = input()
    print(get_number_of_showable_hands(statuses))

if __name__ == '__main__':
    main()


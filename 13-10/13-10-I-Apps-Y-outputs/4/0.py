
def move_cups(moves):
    cup_1 = cup_2 = cup_3 = False
    for move in moves:
        if move == "A":
            cup_1, cup_2 = cup_2, cup_1
        elif move == "B":
            cup_2, cup_3 = cup_3, cup_2
        else:
            cup_1, cup_3 = cup_3, cup_1
    if cup_1:
        return 1
    elif cup_2:
        return 2
    else:
        return 3

def main():
    moves = input()
    print(move_cups(moves))

if __name__ == '__main__':
    main()



def get_possible_values(dice_sides, sum_of_values):
    possible_values = []
    for i in range(1, dice_sides+1):
        if i > sum_of_values:
            break
        possible_values.append(i)
    return possible_values

def get_impossible_values(dice_sides, sum_of_values):
    impossible_values = []
    for i in range(1, dice_sides+1):
        if i <= sum_of_values:
            continue
        impossible_values.append(i)
    return impossible_values

def get_dice_values(dice_sides, sum_of_values):
    possible_values = get_possible_values(dice_sides, sum_of_values)
    impossible_values = get_impossible_values(dice_sides, sum_of_values)
    return possible_values, impossible_values

def main():
    num_dice, sum_of_values = map(int, input().split())
    dice_sides = list(map(int, input().split()))
    possible_values_list = []
    impossible_values_list = []
    for i in range(num_dice):
        possible_values, impossible_values = get_dice_values(dice_sides[i], sum_of_values)
        possible_values_list.append(len(possible_values))
        impossible_values_list.append(len(impossible_values))
    print(*possible_values_list)
    print(*impossible_values_list)

if __name__ == '__main__':
    main()


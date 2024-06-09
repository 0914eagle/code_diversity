
def get_possible_values(dice_values, sum_of_values):
    possible_values = []
    for i in range(1, dice_values+1):
        if i > sum_of_values:
            break
        possible_values.append(i)
    return possible_values

def get_impossible_values(dice_values, sum_of_values):
    impossible_values = []
    for i in range(1, dice_values+1):
        if i > sum_of_values:
            break
        impossible_values.append(sum_of_values-i+1)
    return impossible_values

def get_possible_values_for_each_dice(dice_values, sum_of_values):
    possible_values_for_each_dice = []
    for i in range(len(dice_values)):
        possible_values_for_each_dice.append(get_possible_values(dice_values[i], sum_of_values))
    return possible_values_for_each_dice

def get_impossible_values_for_each_dice(dice_values, sum_of_values):
    impossible_values_for_each_dice = []
    for i in range(len(dice_values)):
        impossible_values_for_each_dice.append(get_impossible_values(dice_values[i], sum_of_values))
    return impossible_values_for_each_dice

def main():
    dice_values = list(map(int, input().split()))
    sum_of_values = int(input())
    possible_values_for_each_dice = get_possible_values_for_each_dice(dice_values, sum_of_values)
    impossible_values_for_each_dice = get_impossible_values_for_each_dice(dice_values, sum_of_values)
    for i in range(len(dice_values)):
        print(len(possible_values_for_each_dice[i]) - len(impossible_values_for_each_dice[i]))

if __name__ == '__main__':
    main()


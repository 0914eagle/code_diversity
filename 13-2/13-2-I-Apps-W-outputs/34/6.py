
def get_possible_values(dice_sides, total_sum):
    possible_values = []
    for i in range(1, dice_sides+1):
        if i > total_sum:
            break
        possible_values.append(i)
    return possible_values

def get_impossible_values(dice_sides, total_sum):
    impossible_values = []
    for i in range(1, dice_sides+1):
        if i <= total_sum:
            impossible_values.append(i)
    return impossible_values

def get_possible_values_for_each_dice(dice_sides_list, total_sum):
    possible_values_list = []
    for dice_sides in dice_sides_list:
        possible_values = get_possible_values(dice_sides, total_sum)
        possible_values_list.append(len(possible_values))
    return possible_values_list

def main():
    dice_sides_list, total_sum = map(int, input().split())
    possible_values_list = get_possible_values_for_each_dice(dice_sides_list, total_sum)
    print(*possible_values_list, sep=' ')

if __name__ == '__main__':
    main()


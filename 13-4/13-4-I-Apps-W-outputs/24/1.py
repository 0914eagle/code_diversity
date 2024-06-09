
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

def get_number_of_possible_values(dice_sides, total_sum):
    return len(get_possible_values(dice_sides, total_sum))

def get_number_of_impossible_values(dice_sides, total_sum):
    return len(get_impossible_values(dice_sides, total_sum))

def main():
    num_dice, total_sum = map(int, input().split())
    dice_sides = list(map(int, input().split()))
    for i in range(num_dice):
        print(get_number_of_impossible_values(dice_sides[i], total_sum))

if __name__ == '__main__':
    main()


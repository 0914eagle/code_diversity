
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

def main():
    n, sum_of_values = map(int, input().split())
    dice_values = [int(input()) for _ in range(n)]
    possible_values = [get_possible_values(dice_value, sum_of_values) for dice_value in dice_values]
    impossible_values = [get_impossible_values(dice_value, sum_of_values) for dice_value in dice_values]
    print(*[len(possible_values[i]) for i in range(n)], sep=' ')

if __name__ == '__main__':
    main()


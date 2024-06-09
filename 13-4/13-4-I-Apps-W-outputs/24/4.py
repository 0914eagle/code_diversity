
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

def get_guaranteed_values(dice_values, sum_of_values):
    guaranteed_values = []
    for i in range(1, dice_values+1):
        if i > sum_of_values:
            break
        guaranteed_values.append(sum_of_values-i+1)
    return guaranteed_values

def main():
    n, sum_of_values = map(int, input().split())
    dice_values = list(map(int, input().split()))
    guaranteed_values = []
    for i in range(n):
        guaranteed_values.append(get_guaranteed_values(dice_values[i], sum_of_values))
    print(*guaranteed_values)

if __name__ == '__main__':
    main()


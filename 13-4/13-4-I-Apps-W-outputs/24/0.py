
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

def main():
    n, sum_of_values = map(int, input().split())
    dice_sides = [int(input()) for _ in range(n)]
    possible_values = [get_possible_values(dice_sides[i], sum_of_values) for i in range(n)]
    impossible_values = [get_impossible_values(dice_sides[i], sum_of_values) for i in range(n)]
    print(*[len(possible_values[i]) for i in range(n)], sep=' ')
    print(*[len(impossible_values[i]) for i in range(n)], sep=' ')

if __name__ == '__main__':
    main()


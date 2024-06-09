
def calculate_time(total_time, monkeys_type_1, monkeys_type_2):
    # Calculate the time it takes for each type of monkey to pick and open all the coconuts
    time_type_1 = 0
    time_type_2 = 0
    for monkey in monkeys_type_1:
        time_type_1 += monkey[0] + (monkey[1] * len(monkeys_type_1))
    for monkey in monkeys_type_2:
        time_type_2 += monkey[0] + (monkey[1] * len(monkeys_type_2))

    # Calculate the time between the arrival of the first type of monkeys and the arrival of the second type
    time_between = total_time - time_type_1 - time_type_2

    return time_between

def main():
    total_time = int(input())
    num_monkeys_type_1 = int(input())
    monkeys_type_1 = []
    for i in range(num_monkeys_type_1):
        monkeys_type_1.append(list(map(int, input().split())))
    num_monkeys_type_2 = int(input())
    monkeys_type_2 = []
    for i in range(num_monkeys_type_2):
        monkeys_type_2.append(list(map(int, input().split())))

    time_between = calculate_time(total_time, monkeys_type_1, monkeys_type_2)
    print(time_between)

if __name__ == '__main__':
    main()


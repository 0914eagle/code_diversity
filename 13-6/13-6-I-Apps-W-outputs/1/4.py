
def find_time_between_arrivals(total_time, first_type_monkeys, second_type_monkeys):
    # Find the time it takes for the first type of monkeys to pick off all the coconuts
    first_type_time = 0
    for monkey in first_type_monkeys:
        first_type_time += monkey[0] + (monkey[1] * total_time)

    # Find the time it takes for the second type of monkeys to open all the coconuts
    second_type_time = 0
    for monkey in second_type_monkeys:
        second_type_time += monkey[0] + (monkey[1] * total_time)

    # Return the difference between the arrival times of the two types of monkeys
    return second_type_time - first_type_time

def main():
    total_time = int(input())
    first_type_monkeys = []
    second_type_monkeys = []

    num_first_type_monkeys = int(input())
    for _ in range(num_first_type_monkeys):
        first_type_monkeys.append(list(map(int, input().split())))

    num_second_type_monkeys = int(input())
    for _ in range(num_second_type_monkeys):
        second_type_monkeys.append(list(map(int, input().split())))

    print(find_time_between_arrivals(total_time, first_type_monkeys, second_type_monkeys))

if __name__ == '__main__':
    main()


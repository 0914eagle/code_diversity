
def get_time_between_arrivals(total_time, monkeys_type1, monkeys_type2):
    # Calculate the time it takes for each type of monkey to pick off all the coconuts
    time_type1 = [monkey[0] + (monkey[1] - 1) * monkey[0] for monkey in monkeys_type1]
    time_type2 = [monkey[0] + (monkey[1] - 1) * monkey[0] for monkey in monkeys_type2]
    
    # Calculate the total time it takes for both types of monkeys to pick off all the coconuts
    total_time_type1 = sum(time_type1)
    total_time_type2 = sum(time_type2)
    
    # Calculate the time between the arrival of the first type of monkeys and the arrival of the second type of monkeys
    time_between_arrivals = total_time - total_time_type1 - total_time_type2
    
    return time_between_arrivals

def main():
    total_time = int(input())
    num_monkeys_type1 = int(input())
    monkeys_type1 = []
    for _ in range(num_monkeys_type1):
        monkeys_type1.append(list(map(int, input().split())))
    num_monkeys_type2 = int(input())
    monkeys_type2 = []
    for _ in range(num_monkeys_type2):
        monkeys_type2.append(list(map(int, input().split())))
    
    print(get_time_between_arrivals(total_time, monkeys_type1, monkeys_type2))

if __name__ == '__main__':
    main()


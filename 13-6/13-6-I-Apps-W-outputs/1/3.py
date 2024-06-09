
def calculate_time_between_arrivals(total_time, monkey_type_1_data, monkey_type_2_data):
    # Initialize variables
    time_spent_by_monkey_type_1 = 0
    time_spent_by_monkey_type_2 = 0
    time_between_arrivals = 0

    # Iterate through the data for monkey type 1
    for monkey_data in monkey_type_1_data:
        # Calculate the time spent by each monkey of type 1
        time_spent_by_monkey_type_1 += monkey_data[0] + (monkey_data[1] * total_time)

    # Iterate through the data for monkey type 2
    for monkey_data in monkey_type_2_data:
        # Calculate the time spent by each monkey of type 2
        time_spent_by_monkey_type_2 += monkey_data[0] + (monkey_data[1] * total_time)

    # Calculate the time between the arrivals
    time_between_arrivals = time_spent_by_monkey_type_1 - time_spent_by_monkey_type_2

    return time_between_arrivals

def main():
    total_time = int(input())
    monkey_type_1_data = []
    monkey_type_2_data = []

    # Read the data for monkey type 1
    num_monkeys_type_1 = int(input())
    for _ in range(num_monkeys_type_1):
        monkey_data = list(map(int, input().split()))
        monkey_type_1_data.append(monkey_data)

    # Read the data for monkey type 2
    num_monkeys_type_2 = int(input())
    for _ in range(num_monkeys_type_2):
        monkey_data = list(map(int, input().split()))
        monkey_type_2_data.append(monkey_data)

    # Calculate the time between the arrivals
    time_between_arrivals = calculate_time_between_arrivals(total_time, monkey_type_1_data, monkey_type_2_data)

    # Print the result
    print(time_between_arrivals)

if __name__ == '__main__':
    main()


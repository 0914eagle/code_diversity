
def find_arrival_time(total_time, monkeys_info):
    # Initialize variables
    arrival_time = 0
    current_time = 0
    coconuts_picked = 0
    coconuts_opened = 0
    monkeys_type = []
    monkeys_speed = []

    # Loop through the monkeys information
    for monkey in monkeys_info:
        # Check the type of monkey
        if monkey[0] == 1:
            # Add the monkey to the first type list
            monkeys_type.append(1)
            # Add the monkey's speed to the list
            monkeys_speed.append(monkey[1])
        else:
            # Add the monkey to the second type list
            monkeys_type.append(2)
            # Add the monkey's speed to the list
            monkeys_speed.append(monkey[1])

    # Loop through the monkeys information
    for i in range(len(monkeys_type)):
        # Check the type of monkey
        if monkeys_type[i] == 1:
            # Calculate the time it takes for the monkey to pick a coconut
            pick_time = monkeys_speed[i]
            # Add the time to the current time
            current_time += pick_time
            # Increment the number of coconuts picked
            coconuts_picked += 1
        else:
            # Calculate the time it takes for the monkey to open a coconut
            open_time = monkeys_speed[i]
            # Add the time to the current time
            current_time += open_time
            # Increment the number of coconuts opened
            coconuts_opened += 1

        # Check if all coconuts have been picked
        if coconuts_picked == coconuts_opened:
            # Calculate the arrival time
            arrival_time = current_time
            # Break the loop
            break

    # Return the arrival time
    return arrival_time

def main():
    # Read the total time and the number of monkeys
    total_time, num_monkeys = map(int, input().split())
    # Read the monkeys information
    monkeys_info = []
    for i in range(num_monkeys):
        monkeys_info.append(list(map(int, input().split())))
    # Find the arrival time
    arrival_time = find_arrival_time(total_time, monkeys_info)
    # Print the arrival time
    print(arrival_time)

if __name__ == '__main__':
    main()


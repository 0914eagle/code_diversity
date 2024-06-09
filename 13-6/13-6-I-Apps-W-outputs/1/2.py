
def get_time_between_arrivals(total_time, monkey_speeds):
    # Initialize variables
    time_spent_picking = 0
    time_spent_opening = 0
    time_between_arrivals = 0

    # Iterate through the monkey speeds
    for monkey_type, speed in monkey_speeds:
        # Calculate the time spent picking or opening coconuts
        if monkey_type == "picking":
            time_spent_picking += speed
        else:
            time_spent_opening += speed

    # Calculate the time between arrivals
    time_between_arrivals = total_time - time_spent_picking - time_spent_opening

    return time_between_arrivals

def main():
    total_time = int(input())
    num_monkeys_picking = int(input())
    monkey_speeds_picking = []
    for _ in range(num_monkeys_picking):
        monkey_speeds_picking.append(tuple(map(int, input().split())))
    num_monkeys_opening = int(input())
    monkey_speeds_opening = []
    for _ in range(num_monkeys_opening):
        monkey_speeds_opening.append(tuple(map(int, input().split())))

    # Create a list of monkey speeds
    monkey_speeds = monkey_speeds_picking + monkey_speeds_opening

    # Calculate the time between arrivals
    time_between_arrivals = get_time_between_arrivals(total_time, monkey_speeds)

    # Print the result
    print(time_between_arrivals)

if __name__ == '__main__':
    main()


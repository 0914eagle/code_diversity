
def calculate_time(total_time, monkey_types):
    # Initialize variables
    time_spent = 0
    monkey_type = 1
    monkey_count = 0
    coconut_count = 0

    # Loop through the total time
    for i in range(total_time):
        # Check if it's time for the next monkey to arrive
        if time_spent == 0 or time_spent % monkey_types[monkey_type-1]["arrival_time"] == 0:
            # Increment the monkey count
            monkey_count += 1

            # Check if it's time for the next coconut to be picked
            if monkey_count % monkey_types[monkey_type-1]["coconut_time"] == 0:
                # Increment the coconut count
                coconut_count += 1

        # Increment the time spent
        time_spent += 1

    # Return the time between the arrival of the first and second types of monkeys
    return time_spent - coconut_count * monkey_types[1]["arrival_time"]

def main():
    # Read the input
    total_time = int(input())
    monkey_types = []
    for i in range(2):
        monkey_types.append({"arrival_time": int(input()), "coconut_time": int(input())})

    # Calculate the time between the arrival of the first and second types of monkeys
    time_between = calculate_time(total_time, monkey_types)

    # Print the output
    print(time_between)

if __name__ == '__main__':
    main()



def get_minimum_minutes(hamsters):
    # Initialize variables
    standing_hamsters = 0
    minutes = 0

    # Iterate through the hamsters and count the standing hamsters
    for hamster in hamsters:
        if hamster == "X":
            standing_hamsters += 1

    # Calculate the minimum number of minutes needed to get the required standing hamsters
    minutes = standing_hamsters // 2

    return minutes

def get_optimal_position(hamsters, minutes):
    # Initialize variables
    standing_hamsters = 0
    optimal_position = ""

    # Iterate through the hamsters and set their position to standing or sitting based on the number of minutes required
    for i in range(len(hamsters)):
        if i < minutes:
            optimal_position += "X"
            standing_hamsters += 1
        else:
            optimal_position += "x"

    # If the number of standing hamsters is odd, switch the position of the last hamster to get an even number
    if standing_hamsters % 2 == 1:
        optimal_position = optimal_position[:-1] + "x" + optimal_position[-1]

    return optimal_position

if __name__ == '__main__':
    while True:
        # Read the input
        hamsters = input().strip()

        # Check if the input is valid
        if len(hamsters) % 2 == 1 or len(hamsters) > 200:
            print("Invalid input")
            continue

        # Calculate the minimum number of minutes needed to get the required standing hamsters
        minutes = get_minimum_minutes(hamsters)

        # Get the optimal position for the hamsters
        optimal_position = get_optimal_position(hamsters, minutes)

        # Print the output
        print(minutes)
        print(optimal_position)


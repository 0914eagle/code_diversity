
def get_minimum_minutes(n, hamsters_position):
    # Initialize variables
    minutes = 0
    standing_hamsters = 0
    desired_standing_hamsters = n // 2

    # Iterate through the hamsters position
    for i in range(n):
        # If the hamster is standing, increase the number of standing hamsters
        if hamsters_position[i] == "X":
            standing_hamsters += 1
        # If the hamster is sitting and the number of standing hamsters is less than the desired number, make the hamster stand up
        elif hamsters_position[i] == "x" and standing_hamsters < desired_standing_hamsters:
            minutes += 1
            standing_hamsters += 1
        # If the hamster is sitting and the number of standing hamsters is greater than the desired number, make the hamster sit down
        elif hamsters_position[i] == "x" and standing_hamsters > desired_standing_hamsters:
            minutes += 1
            standing_hamsters -= 1

    return minutes

def get_optimal_hamsters_position(n, hamsters_position):
    # Initialize variables
    desired_standing_hamsters = n // 2
    standing_hamsters = 0
    optimal_position = ""

    # Iterate through the hamsters position
    for i in range(n):
        # If the hamster is standing, increase the number of standing hamsters
        if hamsters_position[i] == "X":
            standing_hamsters += 1
        # If the hamster is sitting and the number of standing hamsters is less than the desired number, make the hamster stand up
        elif hamsters_position[i] == "x" and standing_hamsters < desired_standing_hamsters:
            optimal_position += "X"
            standing_hamsters += 1
        # If the hamster is sitting and the number of standing hamsters is greater than the desired number, make the hamster sit down
        elif hamsters_position[i] == "x" and standing_hamsters > desired_standing_hamsters:
            optimal_position += "x"
            standing_hamsters -= 1

    return optimal_position

if __name__ == '__main__':
    n = int(input())
    hamsters_position = input()
    minutes = get_minimum_minutes(n, hamsters_position)
    optimal_position = get_optimal_hamsters_position(n, hamsters_position)
    print(minutes)
    print(optimal_position)


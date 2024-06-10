
def get_number_of_showable_hands(statuses):
    # Initialize a counter for the number of showable hands
    num_showable_hands = 0

    # Iterate through the statuses of each player
    for status in statuses:
        # If the status is "ALLIN" or "FOLDED", increment the counter
        if status in ["ALLIN", "FOLDED"]:
            num_showable_hands += 1

    # Return the number of showable hands
    return num_showable_hands

def main():
    # Read the number of cows from stdin
    num_cows = int(input())

    # Read the statuses of each cow from stdin
    statuses = input()

    # Call the function to get the number of showable hands
    num_showable_hands = get_number_of_showable_hands(statuses)

    # Print the number of showable hands
    print(num_showable_hands)

if __name__ == '__main__':
    main()


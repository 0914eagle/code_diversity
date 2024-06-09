
import sys

def get_possible_orderings(names):
    # Initialize the number of possible orderings to 1
    possible_orderings = 1

    # Iterate over the names
    for i in range(len(names)):
        # Get the current name and the next name
        current_name = names[i]
        next_name = names[(i + 1) % len(names)]

        # Check if the current name and the next name start with the same letter sequence
        if current_name[:len(current_name) - 1] == next_name[:len(next_name) - 1]:
            # If they do, increment the number of possible orderings
            possible_orderings += 1

    # Return the number of possible orderings
    return possible_orderings % 1000000007

if __name__ == "__main__":
    # Read the number of names from stdin
    num_names = int(input())

    # Read the names from stdin
    names = []
    for i in range(num_names):
        names.append(input())

    # Get the number of possible orderings
    possible_orderings = get_possible_orderings(names)

    # Print the number of possible orderings
    print(possible_orderings)


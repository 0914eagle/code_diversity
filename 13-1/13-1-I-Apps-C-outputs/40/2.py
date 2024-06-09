
import sys

def get_possible_orderings(names):
    # Initialize the number of possible orderings to 1
    possible_orderings = 1

    # Iterate over the names
    for i in range(len(names)):
        # Get the current name and the next name
        current_name = names[i]
        next_name = names[(i + 1) % len(names)]

        # If the current name and the next name start with the same letter sequence, increment the number of possible orderings
        if current_name[:len(current_name)] == next_name[:len(current_name)]:
            possible_orderings += 1

    return possible_orderings % 1000000007

if __name__ == '__main__':
    num_names = int(input())
    names = []

    for i in range(num_names):
        names.append(input())

    print(get_possible_orderings(names))


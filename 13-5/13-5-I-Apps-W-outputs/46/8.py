
def f1(turn_sequence):
    # Convert the turn sequence to a list of directions
    directions = list(turn_sequence)

    # Initialize a list to store the possible unlock patterns
    unlock_patterns = []

    # Iterate through the directions and add the corresponding pivot to the unlock pattern
    for i in range(len(directions)):
        if directions[i] == 'L':
            unlock_patterns.append(i)
        elif directions[i] == 'R':
            unlock_patterns.append(i + 1)
        elif directions[i] == 'S':
            unlock_patterns.append(i)
        elif directions[i] == 'A':
            unlock_patterns.append(i - 1)
        elif directions[i] == '?':
            unlock_patterns.append(i)
            unlock_patterns.append(i + 1)
            unlock_patterns.append(i - 1)

    # Return the number of possible unlock patterns
    return len(unlock_patterns)

def f2(turn_sequence):
    # Convert the turn sequence to a list of directions
    directions = list(turn_sequence)

    # Initialize a list to store the possible unlock patterns
    unlock_patterns = []

    # Iterate through the directions and add the corresponding pivot to the unlock pattern
    for i in range(len(directions)):
        if directions[i] == 'L':
            unlock_patterns.append(i)
        elif directions[i] == 'R':
            unlock_patterns.append(i + 1)
        elif directions[i] == 'S':
            unlock_patterns.append(i)
        elif directions[i] == 'A':
            unlock_patterns.append(i - 1)
        elif directions[i] == '?':
            unlock_patterns.append(i)
            unlock_patterns.append(i + 1)
            unlock_patterns.append(i - 1)

    # Return the number of possible unlock patterns
    return len(unlock_patterns)

if __name__ == '__main__':
    turn_sequence = input("Enter the turn sequence: ")
    print(f"The number of possible unlock patterns is {f1(turn_sequence)}")


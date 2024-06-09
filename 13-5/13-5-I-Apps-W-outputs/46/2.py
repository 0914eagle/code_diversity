
def f1(turn_sequence):
    # Replace '?' with 'L', 'R', 'S', or 'A' to form a valid turn sequence
    valid_turn_sequence = turn_sequence.replace("?", "L")
    return len(set(valid_turn_sequence))

def f2(turn_sequence):
    # Replace '?' with 'L', 'R', 'S', or 'A' to form a valid turn sequence
    valid_turn_sequence = turn_sequence.replace("?", "R")
    return len(set(valid_turn_sequence))

def f3(turn_sequence):
    # Replace '?' with 'L', 'R', 'S', or 'A' to form a valid turn sequence
    valid_turn_sequence = turn_sequence.replace("?", "S")
    return len(set(valid_turn_sequence))

def f4(turn_sequence):
    # Replace '?' with 'L', 'R', 'S', or 'A' to form a valid turn sequence
    valid_turn_sequence = turn_sequence.replace("?", "A")
    return len(set(valid_turn_sequence))

if __name__ == '__main__':
    turn_sequence = input("Enter a turn sequence with '?' replaced by 'L', 'R', 'S', or 'A': ")
    print(f1(turn_sequence))
    print(f2(turn_sequence))
    print(f3(turn_sequence))
    print(f4(turn_sequence))


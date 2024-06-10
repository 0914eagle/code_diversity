
def get_two_suspects(n, p, coders):
    # Initialize a set to store the two suspects
    suspects = set()
    
    # Iterate over the coders
    for coder in coders:
        # If the coder has agreed with the head's choice, add them to the suspects set
        if coder[0] in suspects or coder[1] in suspects:
            suspects.add(coder[0])
            suspects.add(coder[1])
    
    # Return the number of possible two-suspect sets
    return len(suspects)

def get_number_of_possible_two_suspect_sets(n, p, coders):
    # Initialize a set to store the two suspects
    suspects = set()
    
    # Iterate over the coders
    for coder in coders:
        # If the coder has agreed with the head's choice, add them to the suspects set
        if coder[0] in suspects or coder[1] in suspects:
            suspects.add(coder[0])
            suspects.add(coder[1])
    
    # Return the number of possible two-suspect sets
    return len(suspects)

if __name__ == '__main__':
    n, p = map(int, input().split())
    coders = []
    for _ in range(n):
        x, y = map(int, input().split())
        coders.append((x, y))
    print(get_number_of_possible_two_suspect_sets(n, p, coders))


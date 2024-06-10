
def get_suspects(n, p, coders):
    # Initialize a set to store the suspects
    suspects = set()
    
    # Iterate over the coders
    for coder in coders:
        # If the coder agreed with the head's choice, add their names to the suspects set
        if coder[0] in suspects or coder[1] in suspects:
            suspects.add(coder[0])
            suspects.add(coder[1])
    
    # Return the number of suspects
    return len(suspects)

def get_two_suspects(n, p, coders):
    # Get the number of suspects
    num_suspects = get_suspects(n, p, coders)
    
    # Initialize a set to store the two suspects
    two_suspects = set()
    
    # Iterate over the combinations of two suspects
    for coder1, coder2 in combinations(coders, 2):
        # If the two suspects are agreed upon by at least p coders, add them to the set
        if coder1 in two_suspects or coder2 in two_suspects:
            two_suspects.add(coder1)
            two_suspects.add(coder2)
    
    # Return the number of two-suspect sets
    return len(two_suspects)

if __name__ == '__main__':
    n, p = map(int, input().split())
    coders = []
    for _ in range(n):
        coder = tuple(map(int, input().split()))
        coders.append(coder)
    print(get_two_suspects(n, p, coders))


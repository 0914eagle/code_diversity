
def get_two_suspects(n, p, coders):
    # Initialize a set to store the two suspects
    suspects = set()
    
    # Iterate over the coders and their names
    for coder, names in coders.items():
        # If the coder has at least one name in common with the suspects, add it to the set
        if len(suspects.intersection(names)) > 0:
            suspects.add(coder)
    
    # Return the number of suspects
    return len(suspects)

def get_number_of_two_suspect_sets(n, p, coders):
    # Initialize a variable to store the number of two-suspect sets
    number_of_sets = 0
    
    # Iterate over the coders and their names
    for coder, names in coders.items():
        # If the coder has at least one name in common with the suspects, add it to the set
        if len(suspects.intersection(names)) > 0:
            number_of_sets += 1
    
    # Return the number of two-suspect sets
    return number_of_sets

if __name__ == '__main__':
    n, p = map(int, input().split())
    coders = {}
    for _ in range(n):
        coder, name1, name2 = map(int, input().split())
        if coder not in coders:
            coders[coder] = set()
        coders[coder].add(name1)
        coders[coder].add(name2)
    print(get_number_of_two_suspect_sets(n, p, coders))


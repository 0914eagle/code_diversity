
def get_two_suspects(n, p, coders):
    # Initialize a set to store the chosen suspects
    chosen_suspects = set()
    # Initialize a variable to store the number of agreed people
    num_agreed = 0
    # Loop through each coder
    for coder in coders:
        # If the coder's first choice is in the chosen suspects, add the coder's second choice to the chosen suspects
        if coder[0] in chosen_suspects:
            chosen_suspects.add(coder[1])
        # If the coder's second choice is in the chosen suspects, add the coder's first choice to the chosen suspects
        elif coder[1] in chosen_suspects:
            chosen_suspects.add(coder[0])
        # If neither choice is in the chosen suspects, add both choices to the chosen suspects
        else:
            chosen_suspects.update(coder)
        # Increment the number of agreed people
        num_agreed += 1
        # If the number of agreed people is greater than or equal to p, break out of the loop
        if num_agreed >= p:
            break
    # Return the number of chosen suspects
    return len(chosen_suspects)

def count_two_suspect_sets(n, p, coders):
    # Initialize a variable to store the total number of two-suspect sets
    total_sets = 0
    # Loop through each coder
    for coder in coders:
        # Get the number of two-suspect sets for the current coder
        num_sets = get_two_suspects(n, p, coders[coder:])
        # Increment the total number of two-suspect sets
        total_sets += num_sets
    # Return the total number of two-suspect sets
    return total_sets

if __name__ == '__main__':
    n, p = map(int, input().split())
    coders = []
    for _ in range(n):
        coders.append(tuple(map(int, input().split())))
    print(count_two_suspect_sets(n, p, coders))


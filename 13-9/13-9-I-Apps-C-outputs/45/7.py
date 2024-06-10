
def get_two_suspects(n, p, coders):
    # Initialize a set to store the chosen suspects
    chosen_suspects = set()
    # Initialize a variable to store the number of agreed people
    agreed_people = 0
    # Iterate over the coders
    for coder in coders:
        # If the coder has agreed with the chosen suspects
        if coder[0] in chosen_suspects or coder[1] in chosen_suspects:
            # Increment the number of agreed people
            agreed_people += 1
        # If the number of agreed people is greater than or equal to p
        if agreed_people >= p:
            # Return the number of possible two-suspect sets
            return len(chosen_suspects)
        # If the coder has not agreed with the chosen suspects
        else:
            # Add the coder's suspects to the set of chosen suspects
            chosen_suspects.add(coder[0])
            chosen_suspects.add(coder[1])
    # If the number of agreed people is less than p
    return 0

def main():
    # Read the input
    n, p = map(int, input().split())
    coders = []
    for _ in range(n):
        coders.append(tuple(map(int, input().split())))
    # Call the get_two_suspects function
    result = get_two_suspects(n, p, coders)
    # Print the result
    print(result)

if __name__ == '__main__':
    main()


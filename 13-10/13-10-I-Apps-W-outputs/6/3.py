
def get_party(mp_list):
    # Initialize the party array
    party = []

    # Iterate through the list of MPs
    for mp in mp_list:
        # Check if the MP is already in the party array
        if mp in party:
            # If the MP is already in the party array, continue to the next MP
            continue
        # Otherwise, add the MP to the party array
        party.append(mp)

    # Return the party array
    return party

def main():
    # Read the number of MPs from stdin
    n_mps = int(input())

    # Initialize the list of MPs
    mp_list = []

    # Read the photographs taken from Monday to Friday
    for i in range(5):
        # Read the number of pairs on the current photograph
        n_pairs = int(input())

        # Read the pairs of MPs that are arguing on the current photograph
        for j in range(n_pairs):
            # Read the labels of the MPs that are arguing
            k, l = map(int, input().split())

            # Add the MPs to the list of MPs
            mp_list.append(k)
            mp_list.append(l)

    # Get the party array
    party = get_party(mp_list)

    # Print the party array
    print(" ".join([str(mp) for mp in party]))

if __name__ == '__main__':
    main()


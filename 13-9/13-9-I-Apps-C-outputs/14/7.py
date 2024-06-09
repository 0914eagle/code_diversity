
def number_of_suspects(n, p, names):
    # Initialize a dictionary to store the number of agreements for each coder
    agreements = {i: 0 for i in range(1, n + 1)}

    # Iterate over the names of the coders and increment the agreement count for each coder
    for name in names:
        agreements[name[0]] += 1
        agreements[name[1]] += 1

    # Initialize a set to store the selected suspects
    selected_suspects = set()

    # Iterate over the agreements and select the suspects that have at least p agreements
    for coder, agreement in agreements.items():
        if agreement >= p:
            selected_suspects.add(coder)

    # Return the number of possible two-suspect sets
    return len(selected_suspects) * (len(selected_suspects) - 1) // 2


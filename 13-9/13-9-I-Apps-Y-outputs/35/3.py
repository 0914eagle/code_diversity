
def largest_number_of_pieces_crashed(N):
    # Initialize a list to store the positions of the cuts
    cuts = []

    # Loop through the given number of cuts
    for i in range(N):
        # Add the current cut to the list of cuts
        cuts.append(i)

    # Sort the list of cuts in descending order
    cuts.sort(reverse=True)

    # Initialize a variable to store the largest number of pieces crashed
    largest_number_of_pieces_crashed = 0

    # Loop through the list of cuts
    for i in range(len(cuts)):
        # Calculate the number of pieces crashed for the current cut
        number_of_pieces_crashed = (i + 1) * 2

        # If the number of pieces crashed is greater than the largest number of pieces crashed so far, update the largest number of pieces crashed
        if number_of_pieces_crashed > largest_number_of_pieces_crashed:
            largest_number_of_pieces_crashed = number_of_pieces_crashed

    # Return the largest number of pieces crashed
    return largest_number_of_pieces_crashed


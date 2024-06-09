
def is_possible_to_win(sequence):
    # Initialize variables
    n = len(sequence)
    i = 0
    j = n - 1
    beautiful_word = ""

    # Iterate through the sequence
    while i < j:
        # If the current letter is the rightmost letter, append it to the end of the word
        if i == j:
            beautiful_word += sequence[i]
            break

        # If the current letter is not the rightmost letter, append it to the end of the word
        beautiful_word += sequence[i]

        # Update the indices
        i += 1
        j -= 1

    # Check if the word is beautiful
    if beautiful_word == "":
        return "NE"
    else:
        return "DA"

def get_most_beautiful_word(sequence):
    # Initialize variables
    n = len(sequence)
    i = 0
    j = n - 1
    beautiful_word = ""

    # Iterate through the sequence
    while i < j:
        # If the current letter is the rightmost letter, append it to the end of the word
        if i == j:
            beautiful_word += sequence[i]
            break

        # If the current letter is not the rightmost letter, append it to the end of the word
        beautiful_word += sequence[i]

        # Update the indices
        i += 1
        j -= 1

    return beautiful_word

# Main
n = int(input())
sequence = input()

# Check if it is possible for Slavko to win
if is_possible_to_win(sequence) == "DA":
    print("DA")
    print(get_most_beautiful_word(sequence))
else:
    print("NE")



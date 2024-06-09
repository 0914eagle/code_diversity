
def solve(barbarians, rounds):
    # Initialize a dictionary to store the words on the stone tablets
    tablets = {i: barbarians[i-1] for i in range(1, len(barbarians)+1)}
    # Initialize a set to store the words shown by Tarzan
    shown_words = set()
    # Iterate through the rounds
    for round in rounds:
        # If the round is of the first type, add the shown word to the set of shown words
        if round[0] == 1:
            shown_words.add(round[1])
        # If the round is of the second type, count the number of words on the stone tablet that are a consecutive substring of the shown words
        elif round[0] == 2:
            count = 0
            for word in tablets[round[1]]:
                if word in shown_words:
                    count += 1
            yield count
        else:
            raise ValueError("Invalid round type")


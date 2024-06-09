
def solve(barbarians, rounds):
    # Initialize a dictionary to store the words on the stone tablets
    tablets = {}
    for i, word in enumerate(barbarians):
        tablets[i+1] = word

    # Iterate through the rounds
    for round in rounds:
        # If the round is of the first type, show the word to the barbarians
        if round[0] == 1:
            pass
        # If the round is of the second type, count the number of words on the stone tablets that have the shown word as a consecutive substring
        elif round[0] == 2:
            barbarian = round[1]
            word = round[2]
            count = 0
            for tablet in tablets.values():
                if word in tablet:
                    count += 1
            print(count)




def solve(barbarians, rounds):
    # Initialize a dictionary to store the words on the stone tablets
    tablets = {}
    for i, word in enumerate(barbarians):
        tablets[i+1] = word

    # Iterate through the rounds
    for round in rounds:
        if round[0] == 1:
            # If the round is of the first type, show the word to Tarzan
            pass
        elif round[0] == 2:
            # If the round is of the second type, answer Tarzan's question
            barbarian = round[1]
            word = tablets[barbarian]
            count = 0
            for i in range(len(word)):
                # Check if the word on the stone tablet is a consecutive substring of the shown word
                if word[i:i+len(word)] == word:
                    count += 1
            print(count)
        else:
            # Invalid round type
            pass


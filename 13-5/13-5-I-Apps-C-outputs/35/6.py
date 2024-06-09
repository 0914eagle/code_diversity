
def get_character_type(candidate_names, utterances):
    # Initialize a dictionary to store the character types of each candidate
    character_types = {}
    for candidate in candidate_names:
        character_types[candidate] = None

    # Iterate through each utterance and update the character types of the candidates
    for utterance in utterances:
        # Split the utterance into the name of the speaker and the statement
        speaker, statement = utterance.split(" ")

        # If the statement is a character type claim, update the character type of the speaker
        if statement.startswith("truther") or statement.startswith("fabulist") or statement.startswith("charlatan"):
            character_types[speaker] = statement.split(" ")[0]

        # If the statement is a negation, update the character type of the speaker
        elif statement.startswith("not"):
            character_types[speaker] = "not " + character_types[speaker]

        # If the statement is a conjunction, update the character types of the speakers
        elif statement.startswith("and"):
            speaker1, speaker2 = statement.split(" ")[1:]
            character_types[speaker1] = "and " + character_types[speaker1] + " " + character_types[speaker2]
            character_types[speaker2] = "and " + character_types[speaker1] + " " + character_types[speaker2]

        # If the statement is a disjunction, update the character types of the speakers
        elif statement.startswith("xor"):
            speaker1, speaker2 = statement.split(" ")[1:]
            character_types[speaker1] = "xor " + character_types[speaker1] + " " + character_types[speaker2]
            character_types[speaker2] = "xor " + character_types[speaker1] + " " + character_types[speaker2]

    # Return the character types of the candidates
    return [character_types[candidate] for candidate in candidate_names]

def main():
    # Read the input data
    candidate_names = input().split(" ")
    utterances = []
    for _ in range(int(input())):
        utterances.append(input())

    # Get the character types of the candidates
    character_types = get_character_type(candidate_names, utterances)

    # Print the character types of the candidates
    for character_type in character_types:
        print(character_type)

if __name__ == '__main__':
    main()


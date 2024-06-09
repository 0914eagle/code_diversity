
def get_character_type(candidate_name, transcript):
    # Initialize a dictionary to store the character types of each candidate
    character_types = {}

    # Iterate through the transcript and update the character types of each candidate
    for utterance in transcript:
        speaker_name, statement = utterance.split(" ")
        speaker_name = int(speaker_name)
        statement = statement.split(" ")

        # If the statement is a character type claim, update the character type of the candidate
        if statement[0] in ["truther", "fabulist", "charlatan"]:
            character_types[speaker_name] = statement[0]

        # If the statement is a logical operation, update the character types of the candidates involved
        elif statement[0] in ["and", "xor"]:
            # Get the names of the candidates involved in the statement
            candidate_names = [int(name) for name in statement[1:]]

            # Get the character types of the candidates involved
            candidate_types = [character_types[name] for name in candidate_names]

            # Update the character type of the candidate who made the statement
            character_types[speaker_name] = statement[0]

            # If the statement is an "and" statement, update the character types of the candidates involved
            if statement[0] == "and":
                for name, type in zip(candidate_names, candidate_types):
                    character_types[name] = type

            # If the statement is an "xor" statement, update the character types of the candidates involved
            elif statement[0] == "xor":
                for name, type in zip(candidate_names, candidate_types):
                    if type == "truther":
                        character_types[name] = "fabulist"
                    elif type == "fabulist":
                        character_types[name] = "charlatan"
                    elif type == "charlatan":
                        character_types[name] = "truther"

    # Return the character type of the candidate with the given name
    return character_types[candidate_name]

def main():
    # Read the input data
    N, K = map(int, input().split())
    transcript = [input() for _ in range(K)]

    # Get the character type of each candidate
    character_types = [get_character_type(i+1, transcript) for i in range(N)]

    # Print the character types of the candidates
    for character_type in character_types:
        print(character_type)

if __name__ == '__main__':
    main()


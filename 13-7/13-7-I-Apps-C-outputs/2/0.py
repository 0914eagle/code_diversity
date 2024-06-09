
def get_character_types(debate_transcript):
    # Initialize the dictionary to store the character types of each candidate
    character_types = {}

    # Iterate over the utterances in the debate transcript
    for utterance in debate_transcript:
        # Split the utterance into the name of the speaker and the statement
        speaker, statement = utterance.split(" ")

        # If the statement is a character type claim, update the character type of the speaker
        if statement.startswith("truther") or statement.startswith("fabulist") or statement.startswith("charlatan"):
            character_types[speaker] = statement.split(" ")[0]

    # Return the character types of all candidates
    return [character_types[str(i)] for i in range(1, len(character_types) + 1)]


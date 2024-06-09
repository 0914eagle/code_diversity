
def solve(transcript):
    # Initialize the character types of the candidates as unknown
    character_types = ["unknown"] * len(transcript[0])

    # Iterate over each utterance in the transcript
    for utterance in transcript:
        # Extract the name of the speaker and the uttered statement
        speaker, statement = utterance

        # If the statement is a character type claim, update the character type of the speaker
        if statement.startswith("truther"):
            character_types[speaker - 1] = "truther"
        elif statement.startswith("fabulist"):
            character_types[speaker - 1] = "fabulist"
        elif statement.startswith("charlatan"):
            character_types[speaker - 1] = "charlatan"

    # Return the character types of the candidates
    return character_types


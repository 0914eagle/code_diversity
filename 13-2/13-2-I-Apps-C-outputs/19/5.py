
def solve(transcript):
    # Initialize the character types of the candidates as unknown
    character_types = ["unknown"] * len(transcript)

    # Iterate over the utterances in the transcript
    for utterance in transcript:
        # Split the utterance into the name of the speaker and the statement
        speaker, statement = utterance.split(" ")

        # If the statement is a character type claim, update the character type of the speaker
        if statement.startswith("truther") or statement.startswith("fabulist") or statement.startswith("charlatan"):
            character_types[int(speaker) - 1] = statement.split(" ")[0]

    # Return the character types of the candidates
    return character_types


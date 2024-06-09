
def solve(transcript):
    # Initialize a dictionary to store the character types of each candidate
    character_types = {}

    # Iterate through the transcript
    for utterance in transcript:
        # Split the utterance into its constituent parts
        speaker, statement = utterance.split()

        # If the statement is a character type claim, update the character type of the speaker
        if statement.startswith("truther") or statement.startswith("fabulist") or statement.startswith("charlatan"):
            character_types[speaker] = statement.split()[0]

    # Return the character types of all candidates
    return [character_types[str(i)] for i in range(1, len(character_types) + 1)]



def solve(transcript):
    # Initialize the character types of the candidates as unknown
    character_types = ["unknown"] * len(transcript)

    # Iterate through each utterance in the transcript
    for utterance in transcript:
        # Split the utterance into its constituent parts
        speaker, statement = utterance.split(" ")

        # If the statement is a character type claim
        if statement.startswith("truther") or statement.startswith("fabulist") or statement.startswith("charlatan"):
            # Get the name of the candidate being claimed
            candidate = int(statement.split(" ")[1])

            # Set the character type of the candidate
            character_types[candidate - 1] = statement.split(" ")[0]

    # Return the character types of the candidates
    return character_types


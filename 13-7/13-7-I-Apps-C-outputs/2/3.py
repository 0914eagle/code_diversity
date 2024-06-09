
def solve(transcript):
    # Initialize the character types as unknown
    character_types = ["unknown"] * len(transcript)

    # Iterate over the propositions in the transcript
    for proposition in transcript:
        # If the proposition is a character type claim, update the corresponding character type
        if proposition.startswith(("truther", "fabulist", "charlatan")):
            character_types[int(proposition.split()[1]) - 1] = proposition.split()[0]

    # Return the character types of the candidates
    return character_types


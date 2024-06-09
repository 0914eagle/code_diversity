
def get_character_types(debate_transcript):
    # Initialize the character types dictionary
    character_types = {}

    # Iterate over the utterances in the debate transcript
    for utterance in debate_transcript:
        # Split the utterance into the speaker name and the statement
        speaker_name, statement = utterance.split(" ")

        # If the statement is a character type claim
        if statement.startswith("truther") or statement.startswith("fabulist") or statement.startswith("charlatan"):
            # Get the name of the candidate being claimed
            claimed_candidate = int(statement.split(" ")[1])

            # If the speaker has not yet been claimed
            if speaker_name not in character_types:
                # Claim the speaker as a truther
                character_types[speaker_name] = "truther"

            # If the speaker has been claimed as a truther
            elif character_types[speaker_name] == "truther":
                # If the statement is a truther claim about the speaker
                if statement.startswith("truther " + speaker_name):
                    # Claim the claimed candidate as a truther
                    character_types[claimed_candidate] = "truther"

                # If the statement is a fabulist claim about the speaker
                elif statement.startswith("fabulist " + speaker_name):
                    # Claim the claimed candidate as a fabulist
                    character_types[claimed_candidate] = "fabulist"

                # If the statement is a charlatan claim about the speaker
                elif statement.startswith("charlatan " + speaker_name):
                    # Claim the claimed candidate as a charlatan
                    character_types[claimed_candidate] = "charlatan"

            # If the speaker has been claimed as a fabulist
            elif character_types[speaker_name] == "fabulist":
                # If the statement is a truther claim about the speaker
                if statement.startswith("truther " + speaker_name):
                    # Claim the claimed candidate as a truther
                    character_types[claimed_candidate] = "truther"

                # If the statement is a fabulist claim about the speaker
                elif statement.startswith("fabulist " + speaker_name):
                    # Claim the claimed candidate as a fabulist
                    character_types[claimed_candidate] = "fabulist"

                # If the statement is a charlatan claim about the speaker
                elif statement.startswith("charlatan " + speaker_name):
                    # Claim the claimed candidate as a charlatan
                    character_types[claimed_candidate] = "charlatan"

            # If the speaker has been claimed as a charlatan
            elif character_types[speaker_name] == "charlatan":
                # If the statement is a truther claim about the speaker
                if statement.startswith("truther " + speaker_name):
                    # Claim the claimed candidate as a truther
                    character_types[claimed_candidate] = "truther"

                # If the statement is a fabulist claim about the speaker
                elif statement.startswith("fabulist " + speaker_name):
                    # Claim the claimed candidate as a fabulist
                    character_types[claimed_candidate] = "fabulist"

                # If the statement is a charlatan claim about the speaker
                elif statement.startswith("charlatan " + speaker_name):
                    # Claim the claimed candidate as a charlatan
                    character_types[claimed_candidate] = "charlatan"

    # Return the character types dictionary
    return character_types


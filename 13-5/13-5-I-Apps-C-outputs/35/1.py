
def get_character_type(transcript):
    # Initialize a dictionary to store the character types of each candidate
    character_types = {}

    # Iterate through the transcript and parse the statements
    for statement in transcript:
        # Split the statement into the name of the speaker and the statement itself
        speaker, statement = statement.split(" ", 1)

        # If the statement is a character type claim, update the character type of the speaker
        if statement.startswith("truther") or statement.startswith("fabulist") or statement.startswith("charlatan"):
            character_types[speaker] = statement.split(" ")[0]

    # Return the character types of all candidates
    return character_types

def main():
    # Read the input data from stdin
    N, K = map(int, input().split())
    transcript = [input() for _ in range(K)]

    # Get the character types of all candidates
    character_types = get_character_type(transcript)

    # Print the character types of all candidates
    for i in range(1, N+1):
        print(character_types[str(i)])

if __name__ == '__main__':
    main()


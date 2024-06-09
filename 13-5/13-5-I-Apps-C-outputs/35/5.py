
def f1(N, K, utterances):
    # Initialize a dictionary to store the character types of each candidate
    character_types = {}
    for i in range(1, N+1):
        character_types[i] = "unknown"

    # Iterate through the utterances and update the character types
    for utterance in utterances:
        speaker, statement = utterance.split(" ")
        speaker = int(speaker)
        if statement == "truther":
            character_types[speaker] = "truther"
        elif statement == "fabulist":
            character_types[speaker] = "fabulist"
        elif statement == "charlatan":
            character_types[speaker] = "charlatan"
        elif statement.startswith("not"):
            statement = statement[3:]
            if character_types[speaker] == "truther":
                character_types[speaker] = "fabulist"
            elif character_types[speaker] == "fabulist":
                character_types[speaker] = "truther"
        elif statement.startswith("and"):
            statement = statement[3:]
            statement_list = statement.split(" ")
            if character_types[speaker] == "truther" and character_types[int(statement_list[0])] == "truther":
                character_types[speaker] = "truther"
            elif character_types[speaker] == "fabulist" and character_types[int(statement_list[0])] == "fabulist":
                character_types[speaker] = "fabulist"
            else:
                character_types[speaker] = "charlatan"
        elif statement.startswith("xor"):
            statement = statement[3:]
            statement_list = statement.split(" ")
            if character_types[speaker] == "truther" and character_types[int(statement_list[0])] == "fabulist":
                character_types[speaker] = "charlatan"
            elif character_types[speaker] == "fabulist" and character_types[int(statement_list[0])] == "truther":
                character_types[speaker] = "charlatan"

    # Return the character types of the candidates
    return [character_types[i] for i in range(1, N+1)]

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    N = 7
    K = 100
    utterances = ["1 charlatan 1", "1 not charlatan 1", "1 and fabulist 1 fabulist 2"]
    print(f1(N, K, utterances))


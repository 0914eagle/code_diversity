
def get_character_type(statement):
    if statement == "truther":
        return "truther"
    elif statement == "fabulist":
        return "fabulist"
    elif statement == "charlatan":
        return "charlatan"
    elif statement.startswith("not "):
        return "not " + get_character_type(statement[4:])
    elif statement.startswith("and "):
        return "and " + get_character_type(statement[4:])
    elif statement.startswith("xor "):
        return "xor " + get_character_type(statement[4:])
    else:
        raise ValueError("Invalid statement")

def get_candidate_types(transcript):
    candidate_types = {}
    for line in transcript.splitlines():
        speaker, statement = line.split(" ", maxsplit=1)
        speaker = int(speaker)
        character_type = get_character_type(statement)
        candidate_types[speaker] = character_type
    return candidate_types

def main():
    N, K = map(int, input().split())
    transcript = input()
    candidate_types = get_candidate_types(transcript)
    for i in range(1, N+1):
        print(candidate_types[i])

if __name__ == '__main__':
    main()


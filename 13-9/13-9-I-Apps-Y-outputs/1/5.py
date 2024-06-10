
def get_converse_pairs(characters):
    pairs = []
    for i in range(len(characters)):
        for j in range(i+1, len(characters)):
            if characters[i]["language"] in characters[j]["languages"] or characters[j]["language"] in characters[i]["languages"]:
                pairs.append((characters[i]["name"], characters[j]["name"]))
    return pairs

def get_minimum_set(characters, pairs):
    minimum_set = []
    for pair in pairs:
        if pair[0] not in minimum_set and pair[1] not in minimum_set:
            minimum_set.append(pair[0])
    return minimum_set

def get_characters_to_leave(characters, minimum_set):
    characters_to_leave = []
    for character in characters:
        if character["name"] not in minimum_set:
            characters_to_leave.append(character["name"])
    return characters_to_leave

def main():
    num_characters = int(input())
    characters = []
    for i in range(num_characters):
        name, language = input().split()
        languages = input().split()
        characters.append({"name": name, "language": language, "languages": languages})
    pairs = get_converse_pairs(characters)
    minimum_set = get_minimum_set(characters, pairs)
    characters_to_leave = get_characters_to_leave(characters, minimum_set)
    print(len(characters_to_leave))

if __name__ == '__main__':
    main()


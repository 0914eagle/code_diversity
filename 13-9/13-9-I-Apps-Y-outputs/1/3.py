
def can_converse(characters, character_a, character_b):
    # Check if both characters speak the same language
    if characters[character_a] == characters[character_b]:
        return True
    
    # Check if either character understands the other's language
    if characters[character_a] in characters[character_b]["languages"] or characters[character_b] in characters[character_a]["languages"]:
        return True
    
    # Check if there is a sequence of intermediate languages that can translate the message
    for language in characters[character_a]["languages"]:
        if language in characters[character_b]["languages"]:
            return True
    
    return False

def get_conversation_pairs(characters):
    pairs = []
    for i in range(len(characters)):
        for j in range(i+1, len(characters)):
            if can_converse(characters, i, j):
                pairs.append((i, j))
    return pairs

def get_smallest_conversation_set(characters):
    pairs = get_conversation_pairs(characters)
    smallest_set = []
    for pair in pairs:
        if pair[0] not in smallest_set and pair[1] not in smallest_set:
            smallest_set.append(pair[0])
            smallest_set.append(pair[1])
    return len(smallest_set)

def main():
    num_characters = int(input())
    characters = []
    for _ in range(num_characters):
        name, language = input().split()
        languages = input().split()
        characters.append({"name": name, "language": language, "languages": languages})
    print(get_smallest_conversation_set(characters))

if __name__ == '__main__':
    main()


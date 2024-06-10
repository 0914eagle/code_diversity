
def get_characters_to_leave(characters):
    # Find all pairs of characters that can converse
    converse_pairs = set()
    for i in range(len(characters)):
        for j in range(i+1, len(characters)):
            if can_converse(characters[i], characters[j]):
                converse_pairs.add((i, j))
    
    # Find the smallest subset of characters that covers all converse pairs
    min_characters = []
    for i in range(len(characters)):
        if not any(i in pair for pair in converse_pairs):
            min_characters.append(i)
    
    return len(min_characters)

def can_converse(character1, character2):
    # Check if character1 and character2 can converse directly
    if character1[1] == character2[1]:
        return True
    
    # Check if character1 understands the language of character2
    if character1[1] in character2[2:]:
        return True
    
    # Check if character2 understands the language of character1
    if character2[1] in character1[2:]:
        return True
    
    return False

def main():
    num_characters = int(input())
    characters = []
    for i in range(num_characters):
        name, language = input().split()
        languages = [language]
        for j in range(20):
            language = input()
            if language:
                languages.append(language)
            else:
                break
        characters.append((name, language, languages))
    
    print(get_characters_to_leave(characters))

if __name__ == '__main__':
    main()


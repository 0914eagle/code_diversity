
def get_similarity(character1, character2):
    similarity = 0
    for i in range(len(character1)):
        if character1[i] == character2[i]:
            similarity += 1
    return similarity

def get_original_character(characters):
    features = [0] * len(characters[0])
    for character in characters:
        for i in range(len(character)):
            if character[i] == 1:
                features[i] = 1
    return features

def main():
    n, k = map(int, input().split())
    characters = []
    for _ in range(n):
        characters.append(list(map(int, input())))
    original_character = get_original_character(characters)
    print(*original_character, sep='')

if __name__ == '__main__':
    main()


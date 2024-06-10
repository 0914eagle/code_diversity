
def get_input():
    n, k = map(int, input().split())
    characters = []
    for _ in range(n):
        characters.append(list(map(int, input().strip())))
    return n, k, characters

def get_unique_features(characters):
    unique_features = set()
    for character in characters:
        unique_features |= set(character)
    return unique_features

def get_min_similarity_character(characters):
    unique_features = get_unique_features(characters)
    min_similarity = len(unique_features)
    min_similarity_character = []
    for feature in unique_features:
        if feature not in min_similarity_character:
            min_similarity_character.append(feature)
    return min_similarity_character

def main():
    n, k, characters = get_input()
    min_similarity_character = get_min_similarity_character(characters)
    print(*min_similarity_character)

if __name__ == '__main__':
    main()


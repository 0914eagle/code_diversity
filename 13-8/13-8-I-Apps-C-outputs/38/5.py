
def get_similarity(character1, character2):
    similarity = 0
    for i in range(len(character1)):
        if character1[i] == character2[i]:
            similarity += 1
    return similarity

def create_original_character(characters, k):
    # Initialize the new character with all features disabled
    new_character = [0] * k
    
    # Loop through each feature and enable it if it is not present in any of the existing characters
    for i in range(k):
        feature_enabled = False
        for character in characters:
            if character[i] == 1:
                feature_enabled = True
                break
        if not feature_enabled:
            new_character[i] = 1
    
    return new_character

def main():
    n, k = map(int, input().split())
    characters = []
    for _ in range(n):
        characters.append(list(map(int, input().strip())))
    
    new_character = create_original_character(characters, k)
    print(*new_character)

if __name__ == '__main__':
    main()



def get_character_features(n, k):
    # Initialize a list to store the features of Tira's character
    character_features = [0] * k

    # Loop through each feature and set it to 1 if at least one other character has it
    for feature in range(k):
        for character in range(n):
            if character_features[feature] == 1:
                break
            if character_features[feature] == 0 and characters[character][feature] == 1:
                character_features[feature] = 1

    return "".join(str(feature) for feature in character_features)

def main():
    n, k = map(int, input().split())
    characters = [input() for _ in range(n)]
    print(get_character_features(n, k))

if __name__ == '__main__':
    main()



def get_input():
    n, k = map(int, input().split())
    characters = []
    for _ in range(n):
        characters.append(list(map(int, input())))
    return n, k, characters

def get_features(characters):
    features = [0] * k
    for character in characters:
        for i in range(k):
            if character[i] == 1:
                features[i] += 1
    return features

def get_character(features):
    character = [0] * k
    for i in range(k):
        if features[i] % 2 == 0:
            character[i] = 0
        else:
            character[i] = 1
    return "".join(map(str, character))

def main():
    n, k, characters = get_input()
    features = get_features(characters)
    character = get_character(features)
    print(character)

if __name__ == '__main__':
    main()


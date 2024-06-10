
def get_features(n, k):
    features = []
    for i in range(k):
        features.append(0)
    return features

def get_similarity(features1, features2):
    similarity = 0
    for i in range(len(features1)):
        if features1[i] == features2[i]:
            similarity += 1
    return similarity

def create_character(features, n, k):
    character = get_features(n, k)
    for i in range(k):
        if features[i] == 0:
            character[i] = 1
    return character

def get_best_character(features, n, k):
    best_character = get_features(n, k)
    best_similarity = 0
    for i in range(2**k):
        character = create_character(features, n, k)
        similarity = get_similarity(character, features)
        if similarity > best_similarity:
            best_character = character
            best_similarity = similarity
    return best_character

def main():
    n, k = map(int, input().split())
    features = list(map(int, input()))
    character = get_best_character(features, n, k)
    print(*character)

if __name__ == '__main__':
    main()


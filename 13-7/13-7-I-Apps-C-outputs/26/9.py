
def get_language_pairs(language_pairs):
    language_pairs = sorted(language_pairs)
    return [(language_pairs[i][0], language_pairs[i][1]) for i in range(len(language_pairs))]

def get_matching_pairs(language_pairs):
    language_pairs = get_language_pairs(language_pairs)
    matching_pairs = []
    for i in range(len(language_pairs)):
        for j in range(i+1, len(language_pairs)):
            if language_pairs[i][0] == language_pairs[j][1] and language_pairs[i][1] == language_pairs[j][0]:
                matching_pairs.append((i, j))
    return matching_pairs

def get_matching_translators(language_pairs, translators):
    language_pairs = get_language_pairs(language_pairs)
    translators = sorted(translators)
    matching_pairs = get_matching_pairs(language_pairs)
    matching_translators = []
    for pair in matching_pairs:
        matching_translators.append((translators[pair[0]], translators[pair[1]]))
    return matching_translators

def main():
    num_languages, num_translators = map(int, input().split())
    language_pairs = []
    for _ in range(num_translators):
        language_pair = list(map(int, input().split()))
        language_pairs.append(language_pair)
    matching_translators = get_matching_translators(language_pairs, range(num_translators))
    if len(matching_translators) == 0:
        print("impossible")
    else:
        for pair in matching_translators:
            print(pair[0], pair[1])

if __name__ == '__main__':
    main()


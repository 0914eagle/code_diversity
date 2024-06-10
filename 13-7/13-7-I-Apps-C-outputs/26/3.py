
def get_language_pairs(translators):
    language_pairs = []
    for translator in translators:
        language_pairs.append(set(translator))
    return language_pairs

def get_matching_pairs(language_pairs):
    matching_pairs = []
    for i in range(len(language_pairs)):
        for j in range(i+1, len(language_pairs)):
            if language_pairs[i] & language_pairs[j]:
                matching_pairs.append((i, j))
    return matching_pairs

def get_translator_pairs(matching_pairs, translators):
    translator_pairs = []
    for pair in matching_pairs:
        translator_pairs.append((translators[pair[0]], translators[pair[1]]))
    return translator_pairs

def main():
    N, M = map(int, input().split())
    translators = []
    for _ in range(M):
        translators.append(tuple(map(int, input().split())))
    language_pairs = get_language_pairs(translators)
    matching_pairs = get_matching_pairs(language_pairs)
    if len(matching_pairs) == M/2:
        translator_pairs = get_translator_pairs(matching_pairs, translators)
        for pair in translator_pairs:
            print(pair[0], pair[1])
    else:
        print("impossible")

if __name__ == '__main__':
    main()


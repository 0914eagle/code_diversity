
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

def get_matching(translators):
    language_pairs = get_language_pairs(translators)
    matching_pairs = get_matching_pairs(language_pairs)
    if len(matching_pairs) == len(translators) // 2:
        return matching_pairs
    else:
        return "impossible"

def main():
    N, M = map(int, input().split())
    translators = []
    for _ in range(M):
        translators.append(list(map(int, input().split())))
    print(get_matching(translators))

if __name__ == '__main__':
    main()


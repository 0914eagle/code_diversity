
def get_language_pairs(translators):
    language_pairs = []
    for translator in translators:
        language_pairs.append((translator[0], translator[1]))
    return language_pairs

def get_matching_pairs(language_pairs):
    matching_pairs = []
    for i in range(len(language_pairs)):
        for j in range(i+1, len(language_pairs)):
            if language_pairs[i] == language_pairs[j]:
                matching_pairs.append((i, j))
    return matching_pairs

def get_matching_translators(translators, matching_pairs):
    matching_translators = []
    for pair in matching_pairs:
        matching_translators.append((translators[pair[0]][0], translators[pair[1]][0]))
    return matching_translators

def main():
    n, m = map(int, input().split())
    translators = []
    for _ in range(m):
        translators.append(list(map(int, input().split())))
    language_pairs = get_language_pairs(translators)
    matching_pairs = get_matching_pairs(language_pairs)
    if len(matching_pairs) == m/2:
        matching_translators = get_matching_translators(translators, matching_pairs)
        for pair in matching_translators:
            print(pair[0], pair[1])
    else:
        print("impossible")

if __name__ == '__main__':
    main()


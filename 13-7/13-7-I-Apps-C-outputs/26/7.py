
def read_input():
    N, M = map(int, input().split())
    translators = []
    for _ in range(M):
        translator = tuple(map(int, input().split()))
        translators.append(translator)
    return N, M, translators

def is_valid_pair(translator1, translator2):
    return translator1[0] == translator2[1] or translator1[1] == translator2[0]

def find_matching(translators):
    matching = []
    for translator in translators:
        for matching_translator in translators:
            if is_valid_pair(translator, matching_translator) and translator != matching_translator:
                matching.append((translator[0], matching_translator[0]))
                break
    return matching

def main():
    N, M, translators = read_input()
    matching = find_matching(translators)
    if len(matching) == M/2:
        for pair in matching:
            print(pair[0], pair[1])
    else:
        print("impossible")

if __name__ == '__main__':
    main()



def get_input():
    N, M = map(int, input().split())
    translators = []
    for _ in range(M):
        translator = list(map(int, input().split()))
        translators.append(translator)
    return N, M, translators

def match_translators(N, M, translators):
    matched_pairs = []
    for i in range(M):
        for j in range(i+1, M):
            if translators[i][0] == translators[j][1] or translators[i][1] == translators[j][0]:
                matched_pairs.append([i, j])
                break
    if len(matched_pairs) == M/2:
        return matched_pairs
    else:
        return "impossible"

def print_output(matched_pairs):
    if matched_pairs == "impossible":
        print("impossible")
    else:
        for pair in matched_pairs:
            print(pair[0], pair[1])

if __name__ == '__main__':
    N, M, translators = get_input()
    matched_pairs = match_translators(N, M, translators)
    print_output(matched_pairs)


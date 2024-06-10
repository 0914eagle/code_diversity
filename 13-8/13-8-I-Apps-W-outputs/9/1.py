
def get_correct_bracket_sequences(n):
    if n == 1:
        return ["()"]
    sequences = get_correct_bracket_sequences(n-1)
    result = []
    for sequence in sequences:
        result.append("(" + sequence + ")")
        result.append(sequence + ")")
    return result

def get_maximum_matching(n):
    sequences = get_correct_bracket_sequences(n)
    matching = set()
    for sequence in sequences:
        for i in range(len(sequence)):
            if sequence[i] == "(":
                matching.add((i, i+1))
    return len(matching)

if __name__ == '__main__':
    n = int(input())
    print(get_maximum_matching(n) % (10**9 + 7))



def get_bracket_sequence(n):
    if n == 1:
        return ["()"]
    else:
        sequences = get_bracket_sequence(n-1)
        result = []
        for sequence in sequences:
            result.append("(" + sequence + ")")
            result.append(sequence + ")")
        return result

def get_maximum_matching(n):
    sequences = get_bracket_sequence(n)
    matching = set()
    for sequence in sequences:
        for i in range(len(sequence)-1):
            if sequence[i] == "(" and sequence[i+1] == ")":
                matching.add((sequence[i], sequence[i+1]))
    return len(matching)

if __name__ == '__main__':
    n = int(input())
    print(get_maximum_matching(n) % (10**9 + 7))


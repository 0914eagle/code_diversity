
def get_flag_patterns(S):
    patterns = []
    for i in range(1, S // 2 + 1):
        for j in range(i, S - i + 1):
            if i == j:
                patterns.append(f"{i},{j}")
            elif i + 1 == j:
                patterns.append(f"{i},{j}")
            elif i == 1 and j == S - 1:
                patterns.append(f"{i},{j}")
            elif i == S - 1 and j == 1:
                patterns.append(f"{i},{j}")
            elif i + 1 == j and i != 1 and j != S - 1:
                patterns.append(f"{i},{j}")
            elif i == j and i != 1 and j != S - 1:
                patterns.append(f"{i},{j}")
    return patterns


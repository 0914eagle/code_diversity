
def get_visually_appealing_flag_patterns(S):
    patterns = []
    for i in range(1, S):
        for j in range(i, S):
            if i % 2 == 0 and j % 2 == 1:
                patterns.append(f"{i},{j}")
    return patterns


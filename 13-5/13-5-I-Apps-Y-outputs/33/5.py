
def get_visually_appealing_flag_patterns(S):
    patterns = []
    
    for i in range(2, S+1):
        for j in range(i, S+1):
            if i % 2 == 0 and j % 2 == 1:
                continue
            if i + j > S:
                break
            patterns.append(f"{i},{j}")
    
    return patterns


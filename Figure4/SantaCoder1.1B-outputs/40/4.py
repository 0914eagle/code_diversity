def triples_sum_to_zero(l: list):
    
    if len(l) < 3:
        return False
    for i in range(len(l) - 2):
        if l[i] + l[i + 1] + l[i + 2] == 0:
            return True
    return False



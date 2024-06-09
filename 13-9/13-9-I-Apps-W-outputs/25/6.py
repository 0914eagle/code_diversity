
def is_m_cute(a, b, m):
    if a == b:
        return True, [a]
    
    sequence = [a]
    while sequence[-1] < b:
        next_term = sum(sequence) % m + 1
        sequence.append(next_term)
        if len(sequence) > 50:
            return False, []
    
    if sequence[-1] == b:
        return True, sequence
    else:
        return False, []


def make_a_pile(n):
    
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i + 2)
        else:
            result.append(i + 1)
    return result



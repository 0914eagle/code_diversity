def triples_sum_to_zero(l: list):
    
    # your code here
    l = set(l)
    for i in l:
        for j in l:
            for k in l:
                if i + j + k == 0 and i != j and j != k and k != i:
                    return True
    return False


if __name__ == "
def sort_even(l: list):
    
    l.sort()
    even_indicies = [i for i in range(len(l)) if i % 2 == 0]
    return [l[i] for i in even_indicies]



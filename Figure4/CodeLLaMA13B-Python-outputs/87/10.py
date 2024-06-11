def get_row(lst, x):
    
    return sorted([(i, lst[i].index(x)) for i in range(len(lst)) if x in lst[i]], key=lambda x: (x[0], -x[1]))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not
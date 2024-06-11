def add(lst):
    
    if len(lst) == 0:
        return 0
    if lst[0] % 2 == 0:
        return lst[0] + add(lst[2:])
    else:
        return add(lst[2:])


if __name__ == '__main__
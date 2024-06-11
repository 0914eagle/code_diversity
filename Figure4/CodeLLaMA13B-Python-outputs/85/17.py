def add(lst):
    
    if not lst:
        return 0
    return lst[0] if lst[0] % 2 == 0 and len(lst) == 1 else lst[0] + add(lst[2:])


if __name__ == '__main__':
    print(add([4, 2, 6, 
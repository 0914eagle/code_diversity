def add(lst):
    
    if not lst:
        return 0
    else:
        if lst[0] % 2 == 0:
            return lst[0] + add(lst[2:])
        else:
            return add(lst[1:])


if __name__ == '__main__':
    print(add([4
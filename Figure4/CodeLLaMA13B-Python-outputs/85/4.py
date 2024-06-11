def add(lst):
    
    return sum([lst[i] for i in range(len(lst)) if i % 2 == 0])


if __name__ == '__main__':
    print(add([4, 2, 6, 7]))

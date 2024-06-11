def eat(number, need, remaining):
    
    return [number + need, max(0, remaining - need)]


if __name__ == '__main__':
    print(eat(5, 6,
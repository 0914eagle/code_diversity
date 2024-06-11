def eat(number, need, remaining):
    
    return [number + remaining, max(0, remaining - (need - number))]


if __name__ == '__main__':
    print(eat(5, 6, 10))
    print(eat(4, 8, 9))
    print(eat(1, 10, 10))
    print(eat(2, 11, 5))

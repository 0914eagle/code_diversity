def eat(number, need, remaining):
    
    return [number + need, remaining - need if remaining - need > 0 else 0]


if __name__ == '__main__':
    print(e
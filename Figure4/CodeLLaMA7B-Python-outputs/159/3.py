def eat(number, need, remaining):
    
    return [number + remaining, max(0, remaining - (need - number))]


if __name__ == "__main__":
    print(eat(5,
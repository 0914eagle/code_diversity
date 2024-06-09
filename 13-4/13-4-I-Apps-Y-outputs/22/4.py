
def get_integer_in_mind(symbols):
    integer_in_mind = 0
    for symbol in symbols:
        if symbol == "+":
            integer_in_mind += 1
        else:
            integer_in_mind -= 1
    return integer_in_mind

def main():
    symbols = input()
    print(get_integer_in_mind(symbols))

if __name__ == '__main__':
    main()


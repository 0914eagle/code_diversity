
def get_integer_in_mind(symbols):
    integer = 0
    for symbol in symbols:
        if symbol == "+":
            integer += 1
        else:
            integer -= 1
    return integer

def main():
    symbols = input()
    print(get_integer_in_mind(symbols))

if __name__ == '__main__':
    main()


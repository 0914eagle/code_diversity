
def get_final_value(symbols):
    value = 0
    for symbol in symbols:
        if symbol == "+":
            value += 1
        else:
            value -= 1
    return value

def main():
    symbols = input()
    print(get_final_value(symbols))

if __name__ == '__main__':
    main()


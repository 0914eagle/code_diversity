
def calculate_final_integer(symbols):
    integer = 0
    for symbol in symbols:
        if symbol == '+':
            integer += 1
        elif symbol == '-':
            integer -= 1
    return integer

if __name__ == "__main__":
    symbols = input().strip()
    result = calculate_final_integer(symbols)
    print(result)

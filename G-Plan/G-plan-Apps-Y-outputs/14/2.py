
def calculate_final_integer(symbols):
    integer_in_mind = 0
    for symbol in symbols:
        if symbol == '+':
            integer_in_mind += 1
        elif symbol == '-':
            integer_in_mind -= 1
    return integer_in_mind

if __name__ == "__main__":
    symbols = input().strip()
    result = calculate_final_integer(symbols)
    print(result)

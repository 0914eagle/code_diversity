
def calculate_final_integer(symbols):
    total = 0
    for symbol in symbols:
        if symbol == '+':
            total += 1
        elif symbol == '-':
            total -= 1
    return total

if __name__ == "__main__":
    symbols = input().strip()
    result = calculate_final_integer(symbols)
    print(result)


def calculate_final_integer(s):
    integer_in_mind = 0
    for symbol in s:
        if symbol == '+':
            integer_in_mind += 1
        elif symbol == '-':
            integer_in_mind -= 1
    return integer_in_mind

if __name__ == "__main__":
    s = input().strip()
    result = calculate_final_integer(s)
    print(result)

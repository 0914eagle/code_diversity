
def f1(S):
    result = 0
    for symbol in S:
        if symbol == "+":
            result += 1
        else:
            result -= 1
    return result

